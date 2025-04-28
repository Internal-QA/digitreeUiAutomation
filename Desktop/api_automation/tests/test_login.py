import pytest
from endpoints.auth_endpoints import login_endpoint
from utils.request_handler import send_request
from data.auth_data import valid_login_payload, INVALID_USERNAME, INVALID_PASSWORD
from data.test_data import default_headers

def get_message_from_response(response_data):
    """Helper function to get message from response data, handling both formats"""
    return response_data.get("message") or response_data.get("Message")

@pytest.mark.api
def test_valid_login():
    """Test successful login with valid credentials"""
    response = send_request(
        "POST", 
        login_endpoint, 
        json=valid_login_payload,
        headers=default_headers
    )
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
    response_data = response.json()
    assert get_message_from_response(response_data) is not None, f"Response missing message field: {response_data}"
    assert "status" in response_data, f"Response missing status field: {response_data}"
    assert response_data["status"] is False, f"Expected status to be False, but got {response_data['status']}"

@pytest.mark.api
def test_invalid_credentials():
    """Test login with invalid credentials"""
    invalid_payload = {
        "username": "invaliduser",
        "password": "wrongpassword"
    }
    response = send_request(
        "POST", 
        login_endpoint, 
        json=invalid_payload,
        headers=default_headers
    )
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
    response_data = response.json()
    message = get_message_from_response(response_data)
    assert message is not None, f"Response missing message field: {response_data}"
    assert "Invalid username or password" in message, f"Expected 'Invalid username or password' in message, but got: {message}"
    assert "status" in response_data, f"Response missing status field: {response_data}"
    assert response_data["status"] is False, f"Expected status to be False, but got {response_data['status']}"

@pytest.mark.api
def test_missing_credentials():
    """Test login with missing credentials"""
    response = send_request(
        "POST", 
        login_endpoint, 
        json={},
        headers=default_headers
    )
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
    response_data = response.json()
    assert get_message_from_response(response_data) is not None, f"Response missing message field: {response_data}"
    assert "status" in response_data, f"Response missing status field: {response_data}"
    assert response_data["status"] is False, f"Expected status to be False, but got {response_data['status']}"

@pytest.mark.api
@pytest.mark.parametrize("field", ["username", "password"])
def test_missing_field(field):
    """Test login with missing required fields"""
    payload = valid_login_payload.copy()
    del payload[field]
    response = send_request(
        "POST", 
        login_endpoint, 
        json=payload,
        headers=default_headers
    )
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
    response_data = response.json()
    assert get_message_from_response(response_data) is not None, f"Response missing message field: {response_data}"
    assert "status" in response_data, f"Response missing status field: {response_data}"
    assert response_data["status"] is False, f"Expected status to be False, but got {response_data['status']}" 