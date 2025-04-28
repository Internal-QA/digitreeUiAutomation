import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get current environment from environment variable, default to 'dev'
CURRENT_ENV = os.getenv('ENVIRONMENT', 'dev')

# Environment-specific configurations
ENVIRONMENTS = {
    'dev': {
        'BASE_URL': 'https://d3g8su2w1x0h24.cloudfront.net',
        'AUTH_TOKEN': os.getenv('DEV_AUTH_TOKEN', ''),
    },
    'staging': {
        'BASE_URL': 'https://staging-d3g8su2w1x0h24.cloudfront.net',  # Example staging URL
        'AUTH_TOKEN': os.getenv('STAGING_AUTH_TOKEN', ''),
    },
    'prod': {
        'BASE_URL': 'https://prod-d3g8su2w1x0h24.cloudfront.net',  # Example production URL
        'AUTH_TOKEN': os.getenv('PROD_AUTH_TOKEN', ''),
    }
}

# Get current environment settings
CURRENT_SETTINGS = ENVIRONMENTS.get(CURRENT_ENV, ENVIRONMENTS['dev'])

# Export environment-specific settings
BASE_URL = CURRENT_SETTINGS['BASE_URL']
AUTH_TOKEN = CURRENT_SETTINGS['AUTH_TOKEN'] 