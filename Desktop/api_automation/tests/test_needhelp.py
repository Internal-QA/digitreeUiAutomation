import pytest
from config.settings import BASE_URL, AUTH_TOKEN
from utils.request_handler import send_request

def test_get_help_content():
    """
    Test to validate the Help content structure and sections
    """
    endpoint = f"{BASE_URL}/api/get_documents_by_section"
    headers = {
        "Authorization": "kmuq8h4632zkos90deea0f71kxeyvx98j5r9ncdnqh09cjasw9sh5rkdakx2hrxh"  # Using the provided token
    }
    params = {
        "section": "help"
    }

    response = send_request(
        "GET",
        endpoint,
        headers=headers,
        params=params
    )

    # Verify response status
    assert response.status_code == 200, "Failed to get Help content"
    data = response.json()
    
    # Validate main structure
    assert "Title" in data, "Title field is missing"
    assert "Sections" in data, "Sections field is missing"
    
    # Validate title
    assert data["Title"] == "HELP", "Incorrect title"
    
    # Validate sections structure
    sections = data["Sections"]
    expected_sections = ["Section 1", "Section 2", "Section 3"]
    
    # Check all expected sections exist
    for section in expected_sections:
        assert section in sections, f"Missing section: {section}"
    
    # Validate content in each section
    for section_name, content in sections.items():
        assert isinstance(content, list), f"{section_name} content should be a list"
        assert len(content) == 1, f"{section_name} should have exactly 1 paragraph"
        
        # Validate paragraph content
        paragraph = content[0]
        assert isinstance(paragraph, str), f"Content in {section_name} should be a string"
        assert len(paragraph) > 0, f"Empty paragraph found in {section_name}"
        
        # Validate paragraph content matches expected format
        expected_start = "Lorem ipsum dolor sit amet consectetur"
        assert paragraph.startswith(expected_start), f"Paragraph in {section_name} does not start with expected text"
        
        # Validate paragraph contains key phrases
        key_phrases = [
            "Neque volutpat elit diam",
            "Magna sed rhoncus",
            "Pulvinar augue sit nisl",
            "Massa justo malesuada"
        ]
        for phrase in key_phrases:
            assert phrase in paragraph, f"Missing key phrase '{phrase}' in {section_name}"
