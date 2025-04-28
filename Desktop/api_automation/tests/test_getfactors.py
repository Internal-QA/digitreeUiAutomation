import pytest
from config.settings import BASE_URL, AUTH_TOKEN
from utils.request_handler import send_request

def test_get_factors():
    """
    Test to validate the Factors API response structure and content
    """
    endpoint = f"{BASE_URL}/api/factor"
    headers = {
        "Authorization": AUTH_TOKEN
    }

    response = send_request(
        "GET",
        endpoint,
        headers=headers
    )

    # Verify response status
    assert response.status_code == 200, "Failed to get factors"
    data = response.json()
    
    # Validate main structure
    assert "total" in data, "Missing 'total' field"
    assert "pageNo" in data, "Missing 'pageNo' field"
    assert "perPage" in data, "Missing 'perPage' field"
    assert "pages" in data, "Missing 'pages' field"
    assert "results" in data, "Missing 'results' field"
    
    # Validate pagination fields
    assert isinstance(data["total"], int), "Total should be an integer"
    assert isinstance(data["pageNo"], int), "Page number should be an integer"
    assert isinstance(data["perPage"], int), "Per page should be an integer"
    assert isinstance(data["pages"], int), "Pages should be an integer"
    
    # Validate results is a list
    assert isinstance(data["results"], list), "Results should be a list"
    
    # Validate each factor in results
    for factor in data["results"]:
        # Check required fields
        assert "id" in factor, "Factor missing 'id' field"
        assert "name" in factor, "Factor missing 'name' field"
        assert "kpi__name" in factor, "Factor missing 'kpi__name' field"
        assert "factortype__name" in factor, "Factor missing 'factortype__name' field"
        assert "active" in factor, "Factor missing 'active' field"
        assert "createdOn" in factor, "Factor missing 'createdOn' field"
        assert "weight" in factor, "Factor missing 'weight' field"
        
        # Validate field types
        assert isinstance(factor["id"], int), "Factor id should be an integer"
        assert isinstance(factor["name"], str), "Factor name should be a string"
        assert isinstance(factor["active"], bool), "Active should be a boolean"
        assert isinstance(factor["weight"], list), "Weight should be a list"
        
        # Validate weight structure
        for weight_item in factor["weight"]:
            assert "weight_name" in weight_item, "Weight missing 'weight_name' field"
            assert "weight_value" in weight_item, "Weight missing 'weight_value' field"
            assert "metric_id" in weight_item, "Weight missing 'metric_id' field"
    
    # Validate specific factors exist
    expected_factors = {
        4: "Profitability % of Revenue",
        33: "F&I (per car) Used",
        43: "PVR (per car) Used",
        54: "",
        56: "Financials Test",
        115: "PVR (New & Used)",
        116: "F&I (New & Used)",
        141: "PVR New",
        142: "F&I New",
        149: "testing"
    }
    
    # Create a dictionary of actual factors for easier lookup
    actual_factors = {factor["id"]: factor["name"] for factor in data["results"]}
    
    # Validate all expected factors exist with correct names
    for factor_id, expected_name in expected_factors.items():
        assert factor_id in actual_factors, f"Factor with id {factor_id} is missing"
        assert actual_factors[factor_id] == expected_name, f"Factor {factor_id} name mismatch. Expected: {expected_name}, Got: {actual_factors[factor_id]}"
    
    # Validate no unexpected factors exist
    for factor_id in actual_factors:
        assert factor_id in expected_factors, f"Unexpected factor id found: {factor_id}"
    
    # Validate pagination values
    assert data["total"] == 15, "Incorrect total count"
    assert data["pageNo"] == 1, "Incorrect page number"
    assert data["perPage"] == 10, "Incorrect items per page"
    assert data["pages"] == 2, "Incorrect total pages"
    
    