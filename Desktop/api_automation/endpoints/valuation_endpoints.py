from config.config import BASE_URL

# POST endpoint for creating valuation
valuation_endpoint = f"{BASE_URL}/api/valuation"

# GET endpoint for valuation list
def get_valuation_list_endpoint(per_page=10, page_no=1, query="", username="mohit"):
    """
    Constructs the endpoint URL for getting valuation list with query parameters
    Args:
        per_page (int): Number of items per page
        page_no (int): Page number
        query (str): Search query
        username (str): Username for filtering
    Returns:
        str: Complete endpoint URL with query parameters
    """
    return f"{BASE_URL}/api/valuation?perPage={per_page}&pageNo={page_no}&q={query}&username={username}" 