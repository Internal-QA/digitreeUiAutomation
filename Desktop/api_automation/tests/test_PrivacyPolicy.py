import pytest
from config.settings import BASE_URL, AUTH_TOKEN
from utils.request_handler import send_request

@pytest.mark.api
def test_get_privacy_policy():
    """
    Test to validate the Privacy Policy content structure and sections
    """
    endpoint = f"{BASE_URL}/api/get_documents_by_section"
    headers = {
        "Authorization": "kmuq8h4632zkos90deea0f71kxeyvx98j5r9ncdnqh09cjasw9sh5rkdakx2hrxh"  # Using the provided token
    }
    params = {
        "section": "pp"
    }

    response = send_request(
        "GET",
        endpoint,
        headers=headers,
        params=params
    )

    # Verify response status
    assert response.status_code == 200, "Failed to get Privacy Policy content"
    data = response.json()
    
    # Validate main structure
    assert "Title" in data, "Title field is missing"
    assert "Sections" in data, "Sections field is missing"
    
    # Validate title
    assert data["Title"] == "Privacy and policy", "Incorrect title"
    
    # Validate sections structure
    sections = data["Sections"]
    expected_sections = [
        "Personal Information",
        "Usage Data",
        "Device Information",
        "How We Use Your Information"
    ]
    
    # Check all expected sections exist
    for section in expected_sections:
        assert section in sections, f"Missing section: {section}"
    
    # Validate Personal Information section
    personal_info = sections["Personal Information"]
    expected_personal_info = [
        "Name",
        "Email address",
        "Contact information",
        "User credentials (username and password)"
    ]
    assert personal_info == expected_personal_info, "Personal Information section content mismatch"
    
    # Validate Usage Data section
    usage_data = sections["Usage Data"]
    expected_usage_data = [
        "Log files",
        "IP addresses",
        "Browser type",
        "Page visited",
        "Date and time of access"
    ]
    assert usage_data == expected_usage_data, "Usage Data section content mismatch"
    
    # Validate Device Information section
    device_info = sections["Device Information"]
    expected_device_info = [
        "Device type",
        "Operating system",
        "Unique device identifiers"
    ]
    assert device_info == expected_device_info, "Device Information section content mismatch"
    
    # Validate How We Use Your Information section
    usage_info = sections["How We Use Your Information"]
    expected_usage_info = [
        "Provide and maintain our web app",
        "Improve and personalize user experience",
        "Send you updates, newsletters, and promotional material",
        "Respond to your inquiries and support requests",
        "Analyze usage patterns and trends"
    ]
    assert usage_info == expected_usage_info, "How We Use Your Information section content mismatch"
    