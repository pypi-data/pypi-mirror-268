import logging
import os

from furl import furl
import requests

from . import discovery

logger = logging.getLogger(__name__)


def authenticate(env_name='MLHUB_TOKEN'):
    """
     Authenticate with Discovery

     Returns an OAuth2 Access Token

     If `env_name` provided, the Access Token will be saved
     to the named environment variable

     #### Usage

     ```python
     from atlasai.mlhub import client

     token = client.authenticate(<OPTIONAL_ENV_VARIABLE_NAME>)
     ```
     """

    f = furl(discovery.get_url())
    f.path = 'token'
    url = f.url
    headers = {}
    discovery.include_authorization(url, headers)

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    token = data['access_token']

    if env_name:
        os.environ[env_name] = token

    user_id = data.get('email') or data.get('sub') or 'AtlasAI Employee'
    os.environ['LOGNAME'] = user_id

    return token
