import base64
import json
import logging
import time
from json import JSONDecodeError

import requests

logger = logging.getLogger('echolog')


def unpack(request, default=None):
    request.raise_for_status()
    try:
        return json.loads(request.content)
    except (JSONDecodeError, UnicodeDecodeError):
        return request.content or default


class Us2Cognito:
    def __init__(self, api_url, username, password):
        self.api_url = api_url
        self._username = username
        self._password = password
        self._id_token = ''
        self._refresh_token = ''
        self.user = {}
        self.payload = {}
        self.exp = 0
        self.is_api_key = username == '__token__'
        if self.is_api_key:
            self.get_user()
        else:
            self.authenticate()

    def expired(self):
        return time.time() > self.exp

    @property
    def seconds_till_expiry(self):
        return self.exp - time.time()

    def unpack_auth(self, request):
        data = unpack(request)
        auth = data['AuthenticationResult']
        self._id_token = auth['IdToken']
        self._refresh_token = auth.get('RefreshToken', self._refresh_token)
        self.payload = json.loads(base64.b64decode(self._id_token.split('.')[1] + '===').decode())
        self.exp = self.payload['exp']
        self.get_user()

    def get_user(self):
        self.user = unpack(requests.get(f"{self.api_url}/users/current", headers=self.get_headers()))

    def authenticate(self):
        self.unpack_auth(
            requests.post(f"{self.api_url}/users/login", json={'username': self._username, 'password': self._password}),
        )

    def refresh(self):
        try:
            self.unpack_auth(
                requests.post(f"{self.api_url}/users/refresh", json={'refreshToken': self._refresh_token}),
            )
        except Exception as exc:
            logger.warning(f'Failed to renew token due to {exc}, re-authenticating')
            self.authenticate()

    def get_id_token(self):
        if self.seconds_till_expiry <= 5 * 60:
            self.refresh()
        return self._id_token

    def customer(self):
        groups = self.user.get('permissions', [])
        s3 = [g for g in groups if g.startswith('s3-')]
        if s3:
            return s3[0].split('-', 1)[1]
        if 'upload' in groups or 'admin' in groups:
            return self.user.get('cognito_id')

    def regions(self):
        groups = self.user.get('permissions', [])
        return [r.split('-', 1)[1] for r in groups if r.startswith('region-') and 'global' not in r]

    def get_headers(self):
        if self.is_api_key:
            return {"Authorization": f"Api-Key {self._password}"}
        return {"Authorization": f"Bearer {self.get_id_token()}"}

    def get_cookies(self):
        return {".idToken": self.get_id_token()}
