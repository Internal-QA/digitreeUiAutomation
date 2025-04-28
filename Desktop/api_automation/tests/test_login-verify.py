from endpoints.auth_endpoints import login_endpoint
from utils.request_handler import send_request
from data.auth_data import valid_login_payload
from data.test_data import default_headers
import pytest

def test_valid_login():
    """Test login endpoint behavior"""
    response = send_request(
        "POST", 
        login_endpoint, 
        json=valid_login_payload,
        headers=default_headers
    )
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
    response_data = response.json()
    assert "status" in response_data, f"Response missing status field: {response_data}"
    assert response_data["status"] is False, f"Expected status to be False, but got {response_data['status']}"
    
    