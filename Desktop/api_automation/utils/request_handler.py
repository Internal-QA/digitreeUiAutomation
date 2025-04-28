import requests
from utils.logger import get_logger
from config.config import TEST_TIMEOUT, MAX_RETRIES

# Initialize logger for request handling
logger = get_logger()

def send_request(method, url, **kwargs):
    """
    Send HTTP requests with retry mechanism and logging.
    
    This function handles all API requests with the following features:
    - Automatic retry on failure
    - Request timeout handling
    - Detailed logging
    - Error handling
    
    Parameters:
        method (str): HTTP method to use (GET, POST, PUT, DELETE)
        url (str): The URL to send the request to
        **kwargs: Additional arguments for the request:
            - headers: Request headers
            - json: JSON data for POST/PUT requests
            - params: Query parameters
            - data: Form data
            - files: Files to upload
            - timeout: Request timeout (overrides default)
    
    Returns:
        requests.Response: The response object from the request
    
    Raises:
        requests.exceptions.RequestException: If all retry attempts fail
    
    Example:
        # Send a GET request
        response = send_request('GET', 'https://api.example.com/data')
        
        # Send a POST request with JSON data
        response = send_request('POST', 'https://api.example.com/create',
                              json={'name': 'test'})
    """
    # Try the request multiple times if it fails
    for attempt in range(MAX_RETRIES):
        try:
            # Log the request details
            logger.info(f"Sending {method} request to {url}")
            
            # Make the HTTP request
            response = requests.request(
                method=method,      # HTTP method (GET, POST, etc.)
                url=url,           # Target URL
                timeout=TEST_TIMEOUT,  # Request timeout in seconds
                **kwargs           # Additional request parameters
            )
            
            # Log the response status
            logger.info(f"Response status code: {response.status_code}")
            
            # Return the response if successful
            return response
            
        except requests.exceptions.RequestException as e:
            # Log the error and retry if attempts remain
            logger.error(f"Request failed (attempt {attempt + 1}/{MAX_RETRIES}): {str(e)}")
            
            # If this was the last attempt, raise the exception
            if attempt == MAX_RETRIES - 1:
                raise 