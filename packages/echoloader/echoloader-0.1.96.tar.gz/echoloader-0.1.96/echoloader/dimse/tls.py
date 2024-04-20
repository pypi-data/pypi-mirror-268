import base64
import logging
import ssl
import tempfile

from echoloader.config import get_env_var

logger = logging.getLogger('echolog')
DEFAULT_AE_TITLE = "Us2.ai"


def tls_certs():
    cert_str = get_env_var("CA_CERT_DATA")
    key_str = get_env_var("PRIVATE_KEY_DATA")

    if not cert_str or not key_str:
        logger.warning('Missing CA_CERT_DATA or PRIVATE_KEY_DATA, trying to read CA_CERT_DATA_FILE')
        cert_file = get_env_var("CA_CERT_DATA_FILE")
        key_file = get_env_var("PRIVATE_KEY_DATA_FILE")
        if cert_file and key_file:
            return [None, cert_file, key_file]

        raise ValueError('Missing CA_CERT_DATA_FILE or PRIVATE_KEY_DATA_FILE')

    cert_bytes = base64.b64decode(cert_str if cert_str.endswith('==') else cert_str + '==')
    key_bytes = base64.b64decode(key_str if key_str.endswith('==') else key_str + '==')

    cert_file = tempfile.NamedTemporaryFile(delete=False)
    cert_file.write(cert_bytes)
    cert_file.close()

    key_file = tempfile.NamedTemporaryFile(delete=False)
    key_file.write(key_bytes)
    key_file.close()

    return [None, cert_file.name, key_file.name]


def server_context(ca, cert, key):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.verify_mode = ssl.CERT_OPTIONAL
    context.load_cert_chain(certfile=cert, keyfile=key)
    context.load_verify_locations(cafile=ca) if ca else None
    # Only TLS <= 1.2 is supported, make sure we always use this
    context.minimum_version = context.maximum_version = ssl.TLSVersion.TLSv1_2

    return context


def client_context(args):
    context = ssl.create_default_context(
        ssl.Purpose.SERVER_AUTH,
        cafile=args.ca if args.ca else None,
        cadata=args.ca_data if args.ca_data else None,
    )
    context.verify_mode = ssl.CERT_REQUIRED
    context.minimum_version = context.maximum_version = ssl.TLSVersion.TLSv1_2
    if args.cert and args.key and not args.anonymous_tls:
        context.load_cert_chain(certfile=args.cert, keyfile=args.key)
    context.check_hostname = False

    return context
