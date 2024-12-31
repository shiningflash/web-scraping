import os
from dotenv import load_dotenv

def load_environment_variables():
    """
    Load environment variables from a .env file.
    Raises:
        RuntimeError: If required environment variables are missing.
    """
    load_dotenv()

    # Ensure critical environment variables are set
    required_vars = ['LEETCODE_LOGIN_USERNAME', 'LEETCODE_LOGIN_PASSWORD']
    missing_vars = [var for var in required_vars if os.getenv(var) is None]

    if missing_vars:
        raise RuntimeError(f"Missing required environment variables: {', '.join(missing_vars)}")

# Load environment variables
load_environment_variables()

# Application Constants
REMOTE_DEBUGGING_URL = 'http://127.0.0.1:9222'

LEETCODE_LOGIN_URL = 'https://leetcode.com/accounts/login/'
LEETCODE_HOMEPAGE_URL = 'https://leetcode.com/'
LEETCODE_PROBLETSET_PAGE_URL = 'https://leetcode.com/problemset/'


# Leetcode Credentials
LEETCODE_LOGIN_USERNAME = os.getenv('LEETCODE_LOGIN_USERNAME')
LEETCODE_LOGIN_PASSWORD = os.getenv('LEETCODE_LOGIN_PASSWORD')
