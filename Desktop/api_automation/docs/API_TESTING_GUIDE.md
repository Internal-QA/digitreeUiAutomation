# API Testing Guide

This guide provides step-by-step instructions for common API testing scenarios.

## Table of Contents
1. [Basic GET Request](#basic-get-request)
2. [Basic POST Request](#basic-post-request)
3. [Query Parameters](#query-parameters)
4. [Request Headers](#request-headers)
5. [Response Validation](#response-validation)
6. [Error Handling](#error-handling)
7. [Pagination](#pagination)
8. [Search Functionality](#search-functionality)

## Basic GET Request

```python
def test_basic_get():
    # 1. Set up headers
    headers = default_headers.copy()
    headers["Authorization"] = AUTH_TOKEN
    
    # 2. Send GET request
    response = send_request(
        "GET",
        your_endpoint,
        headers=headers
    )
    
    # 3. Verify response
    assert response.status_code == 200
```

## Basic POST Request

```python
def test_basic_post():
    # 1. Set up headers
    headers = default_headers.copy()
    headers["Authorization"] = AUTH_TOKEN
    
    # 2. Set up payload
    payload = {
        "field1": "value1",
        "field2": "value2"
    }
    
    # 3. Send POST request
    response = send_request(
        "POST",
        your_endpoint,
        json=payload,
        headers=headers
    )
    
    # 4. Verify response
    assert response.status_code == 200
```

## Query Parameters

```python
def test_with_query_params():
    # 1. Set up headers
    headers = default_headers.copy()
    headers["Authorization"] = AUTH_TOKEN
    
    # 2. Add query parameters to endpoint
    endpoint = f"{your_endpoint}?param1=value1&param2=value2"
    
    # 3. Send request
    response = send_request(
        "GET",
        endpoint,
        headers=headers
    )
    
    # 4. Verify response
    assert response.status_code == 200
```

## Request Headers

```python
def test_with_custom_headers():
    # 1. Set up custom headers
    headers = default_headers.copy()
    headers["Authorization"] = AUTH_TOKEN
    headers["Custom-Header"] = "custom-value"
    headers["Content-Type"] = "application/json"
    
    # 2. Send request
    response = send_request(
        "GET",
        your_endpoint,
        headers=headers
    )
    
    # 3. Verify response
    assert response.status_code == 200
```

## Response Validation

```python
def test_response_validation():
    # 1. Send request
    response = send_request(...)
    
    # 2. Parse response
    response_data = response.json()
    
    # 3. Validate response structure
    assert "field1" in response_data
    assert "field2" in response_data
    
    # 4. Validate field types
    assert isinstance(response_data["field1"], str)
    assert isinstance(response_data["field2"], int)
    
    # 5. Validate field values
    assert response_data["field1"] == "expected_value"
    assert response_data["field2"] > 0
```

## Error Handling

```python
def test_error_scenarios():
    # 1. Test invalid token
    headers = default_headers.copy()
    headers["Authorization"] = "Token invalid_token"
    response = send_request("GET", your_endpoint, headers=headers)
    assert response.status_code == 401
    
    # 2. Test missing required field
    payload = {"field1": "value1"}  # missing required field2
    response = send_request("POST", your_endpoint, json=payload)
    assert response.status_code == 400
```

## Pagination

```python
def test_pagination():
    # 1. Set up headers
    headers = default_headers.copy()
    headers["Authorization"] = AUTH_TOKEN
    
    # 2. Test first page
    endpoint = f"{your_endpoint}?perPage=10&pageNo=1"
    response = send_request("GET", endpoint, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["results"]) <= 10
    
    # 3. Test second page
    endpoint = f"{your_endpoint}?perPage=10&pageNo=2"
    response = send_request("GET", endpoint, headers=headers)
    assert response.status_code == 200
```

## Search Functionality

```python
def test_search():
    # 1. Set up headers
    headers = default_headers.copy()
    headers["Authorization"] = AUTH_TOKEN
    
    # 2. Test search with query
    endpoint = f"{your_endpoint}?q=search_term"
    response = send_request("GET", endpoint, headers=headers)
    assert response.status_code == 200
    
    # 3. Verify search results
    response_data = response.json()
    for item in response_data["results"]:
        assert "search_term" in item["name"].lower()
```

## Tips and Best Practices

1. **Always validate response status codes**
   - 200: Success
   - 400: Bad Request
   - 401: Unauthorized
   - 403: Forbidden
   - 404: Not Found
   - 500: Server Error

2. **Use descriptive test names**
   - `test_create_valuation_success`
   - `test_create_valuation_invalid_token`
   - `test_get_valuation_list_pagination`

3. **Add clear comments**
   - Explain what each test is doing
   - Document expected behavior
   - Note any special conditions

4. **Handle different response formats**
   - Check for both success and error formats
   - Handle optional fields
   - Validate data types

5. **Use helper functions**
   - For common assertions
   - For response parsing
   - For error handling 