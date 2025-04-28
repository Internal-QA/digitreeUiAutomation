import pytest
from config.settings import BASE_URL, AUTH_TOKEN, CURRENT_ENV
from utils.request_handler import send_request

def test_environment_setup():
    """Example test showing how to use environment settings with actual URL"""
    # Print current environment and URL
    print(f"Running tests in {CURRENT_ENV} environment")
    print(f"Using API URL: {BASE_URL}")
    
    # Example endpoint using the actual base URL
    login_endpoint = f"{BASE_URL}/api/login"
    
    # Use the environment-specific AUTH_TOKEN
    headers = {
        "Authorization": AUTH_TOKEN,
        "Content-Type": "application/json"
    }
    
    # Example request using actual URL
    response = send_request(
        "POST",
        login_endpoint,
        headers=headers,
        json={"username": "test_user", "password": "test_pass"}
    )
    
    # Assertions
    assert response.status_code == 200
    print(f"Successfully connected to {BASE_URL}")

def test_switch_environments():
    """Example showing how to check and use different environments"""
    if CURRENT_ENV == "dev":
        print(f"Running in development environment at {BASE_URL}")
        # Add dev-specific test logic
        assert "d3g8su2w1x0h24.cloudfront.net" in BASE_URL
    elif CURRENT_ENV == "staging":
        print(f"Running in staging environment at {BASE_URL}")
        # Add staging-specific test logic
        assert "staging" in BASE_URL
    elif CURRENT_ENV == "prod":
        print(f"Running in production environment at {BASE_URL}")
        # Add production-specific test logic
        assert "prod" in BASE_URL
    else:
        print(f"Unknown environment: {CURRENT_ENV}") 