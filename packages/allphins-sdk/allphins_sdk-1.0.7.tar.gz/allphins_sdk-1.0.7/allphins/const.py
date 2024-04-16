"""Constants for the project."""
import os

ALLPHINS_API_URL = f"{os.environ.get('ALLPHINS_URL', 'https://app.allphins.com')}/api/v1"
ACCESS_TOKEN_URL = f'{ALLPHINS_API_URL}/token/'
REFRESH_TOKEN_URL = f'{ALLPHINS_API_URL}/token/refresh/'
SSL_IGNORE = os.environ.get('SSL_IGNORE', 'False').lower() in ('true', '1', 'yes')

GET = 'GET'
POST = 'POST'

ISO_8601 = '%Y-%m-%d'
