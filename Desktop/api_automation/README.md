# API Automation Framework

A simple and easy-to-use API testing framework built with Python and Pytest. This framework helps you test APIs with these features:
- Simple test case creation
- Detailed logging
- Test reports
- Retry for failed requests
- Support for different API response formats
- Support for multiple environments (dev, staging, prod)

## Getting Started

### 1. Setup
```bash
# Get the code
git clone <repository-url>
cd api_automation

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 2. Setup Configuration
Create a `.env` file in the main folder:
```bash
# Set the environment you want to test against
ENVIRONMENT=dev  # Options: dev, staging, prod

# Environment-specific tokens
DEV_AUTH_TOKEN=Token your-dev-token
STAGING_AUTH_TOKEN=Token your-staging-token
PROD_AUTH_TOKEN=Token your-prod-token
```

### 3. Environment URLs
The framework uses these base URLs for different environments:
- Development: https://d3g8su2w1x0h24.cloudfront.net
- Staging: https://staging-d3g8su2w1x0h24.cloudfront.net
- Production: https://prod-d3g8su2w1x0h24.cloudfront.net

### 4. Switching Environments
To switch between environments, simply change the ENVIRONMENT value in your .env file:
- For development: ENVIRONMENT=dev
- For staging: ENVIRONMENT=staging
- For production: ENVIRONMENT=prod

## Project Structure

```
api_automation/
├── config/                 # Settings files
│   ├── config.py          # API settings
│   └── settings.py        # Environment settings
│
├── data/                  # Test data
│   ├── test_data.py      # Test data
│   ├── auth_data.py      # Login data
│   └── valuation_data.py # Valuation data
│
├── endpoints/            # API endpoints
│   ├── auth_endpoints.py
│   └── valuation_endpoints.py
│
├── tests/               # Test files
│   ├── test_auth.py
│   └── test_valuation.py
│
├── utils/               # Helper functions
│   ├── request_handler.py
│   └── logger.py
│
├── logs/               # Log files
├── reports/           # Test reports
├── docs/             # Documentation
├── conftest.py       # Pytest setup
├── pytest.ini        # Pytest settings
└── requirements.txt  # Required packages
```

## Writing Tests

### Example: Creating a Valuation
```python
# tests/test_valuation.py
def test_create_valuation():
    # 1. Set up headers
    headers = default_headers.copy()
    headers["Authorization"] = AUTH_TOKEN
    
    # 2. Set up endpoint
    endpoint = f"{valuation_endpoint}?username=mohit"
    
    # 3. Send request
    response = send_request(
        "POST",
        endpoint,
        json=valid_valuation_payload,
        headers=headers
    )
    
    # 4. Check response
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["Status"] is True
```

## Common Tasks

### 1. Adding a New Endpoint
1. Create new file in `endpoints/` folder
2. Add the endpoint URL
3. Add any needed parameters

Example:
```python
# endpoints/valuation_endpoints.py
from config.config import BASE_URL

valuation_endpoint = f"{BASE_URL}/api/valuation"

def get_valuation_list_endpoint(per_page=10, page_no=1, query="", username="mohit"):
    return f"{BASE_URL}/api/valuation?perPage={per_page}&pageNo={page_no}&q={query}&username={username}"
```

### 2. Adding a New Test
1. Create new file in `tests/` folder
2. Import needed modules
3. Write test functions

Example:
```python
# tests/test_valuation.py
import pytest
from endpoints.valuation_endpoints import valuation_endpoint
from utils.request_handler import send_request

def test_new_feature():
    # Add test data
    # Send request
    # Check response
```

### 3. Running Tests
```bash
# Run all tests
python3 -m pytest

# Run one test file
python3 -m pytest tests/test_valuation.py

# Run with more details
python3 -m pytest -v

# Run with HTML report
python3 -m pytest --html=reports/html/report.html
```

## Understanding Test Results

### Test Status
- PASSED: Test worked correctly
- FAILED: Test had an error
- SKIPPED: Test was not run

### Error Messages
When a test fails, you will see:
- Which test failed
- Expected result
- Actual result
- Line number of the error

## Fixing Common Problems

### Common Issues

1. Login Problems
   - Check AUTH_TOKEN in config/config.py
   - Make sure token format is correct: "Token your-token-here"

2. Request Timeouts
   - Check internet connection
   - Check BASE_URL is correct
   - Check if API is working

3. Response Errors
   - Check expected response format
   - Check field names
   - Check data types

## Helpful Links

- [Pytest Documentation](https://docs.pytest.org/)
- [Requests Library](https://docs.python-requests.org/)
- [Python Testing Guide](https://docs.python-guide.org/writing/tests/)

## Getting Help

1. Check the docs folder
2. Look at examples in docs/examples/
3. Read error messages
4. Ask for help in issues section 