import pytest
from config.settings import BASE_URL, AUTH_TOKEN
from utils.request_handler import send_request

def test_get_termAndCond():
    """
    Test to Validate the term And Conditions
    """
    endpoint = f"{BASE_URL}/api/get_documents_by_section"
    headers = {
        "Authorization": "kmuq8h4632zkos90deea0f71kxeyvx98j5r9ncdnqh09cjasw9sh5rkdakx2hrxh"  # Using the provided token
    }
    params={
        "section":"tc"
    }

    response = send_request(
        "GET" , endpoint ,headers=headers , params=params
    )

    # Verify response status
    assert response.status_code == 200, "Failed to get Terms & Conditions content"
    data = response.json()
    
    # Validate main structure
    assert "Title" in data, "Title field is missing"
    assert "Sections" in data, "Sections field is missing"
    
    # Validate title
    assert data["Title"] == "Terms & Conditions", "Incorrect title"
    
    # Validate sections structure
    sections = data["Sections"]
    assert len(sections) == 3, "Expected 3 sections"
    assert "Section 1" in sections, "Section 1 is missing"
    assert "Section 2" in sections, "Section 2 is missing"
    assert "Section 3" in sections, "Section 3 is missing"
    
    # Validate content in each section
    for section_name, content in sections.items():
        assert isinstance(content, list), f"{section_name} content should be a list"
        for paragraph in content:
            assert isinstance(paragraph, str), f"Content in {section_name} should be strings"
            assert len(paragraph) > 0, f"Empty paragraph found in {section_name}"
    
    # Validate specific section lengths
    assert len(sections["Section 1"]) == 3, "Section 1 should have 3 paragraphs"
    assert len(sections["Section 2"]) == 3, "Section 2 should have 3 paragraphs"
    assert len(sections["Section 3"]) == 1, "Section 3 should have 1 paragraph"
    