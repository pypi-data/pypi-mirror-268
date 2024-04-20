import logging
import os
import boto3

logger = logging.getLogger('echolog')

OS_VAR_PREFIX = 'US2_'
SSM_PREFIX = 'SSM_'

DEFAULT_PORT = 11112
DEFAULT_TLS_PORT = 11113


def retrieve_ssm(v):
    try:
        client = boto3.client('ssm', region_name='us-east-1')
        return client.get_parameter(Name=v, WithDecryption=True)['Parameter']['Value']
    except Exception as exc:
        logger.error(f"Failed to fetch ssm parameter {v}")
        raise exc


def get_env_var(key, config_prefix='PACS_', default=None):
    env_value = os.environ.get(f'{OS_VAR_PREFIX}{config_prefix}{key}', default)

    if env_value is None:
        ssm_key = os.environ.get(f'{OS_VAR_PREFIX}{config_prefix}{SSM_PREFIX}{key}', default)
        if ssm_key is None:
            logger.error(f"Failed to fetch ssm parameter {key}")
            return None

        env_value = retrieve_ssm(ssm_key)
    return env_value
