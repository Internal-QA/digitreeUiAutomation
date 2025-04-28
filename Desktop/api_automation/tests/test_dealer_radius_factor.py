import pytest
from config.settings import BASE_URL, AUTH_TOKEN
from utils.request_handler import send_request

@pytest.mark.api
def test_get_dealer_radius_factor():
    """
    Test to validate the dealer radius factor API response
    """
    endpoint = f"{BASE_URL}/api/dealer_radius_factor"
    headers = {
        "Authorization": AUTH_TOKEN
    }
    params = {
        "type": "StepsOptions"
    }

    response = send_request(
        "GET",
        endpoint,
        headers=headers,
        params=params
    )

    # Verify response status
    assert response.status_code == 200, "Failed to get dealer radius factor"
    data = response.json()
    
    # Validate response is a list
    assert isinstance(data, list), "Response should be a list"
    
    # Validate expected values exist
    expected_values = [1, 2, 3, 4, 5, 7, 10, 15, 20, 30, 40, 50, 75, 100]
    
    # Check all expected values are present
    for value in expected_values:
        assert value in data, f"Value {value} is missing from response"
    
    # Validate no unexpected values exist
    for value in data:
        assert value in expected_values, f"Unexpected value {value} found in response"
    
    # Validate values are in ascending order
    assert data == sorted(data), "Values are not in ascending order"
    
    # Validate all values are integers
    for value in data:
        assert isinstance(value, int), f"Value {value} is not an integer"
    
    # Validate minimum and maximum values
    assert min(data) == 1, "Minimum value should be 1"
    assert max(data) == 100, "Maximum value should be 100"