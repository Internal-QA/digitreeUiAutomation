import pytest
from utils.logger import get_logger
import os

logger = get_logger()

@pytest.fixture(scope="session")
def setup_logging():
    """Setup logging for test session"""
    logger.info("Starting test session")
    yield
    logger.info("Ending test session")

@pytest.fixture(autouse=True)
def log_test_info(request):
    """Log test information before and after each test"""
    logger.info(f"Starting test: {request.node.name}")
    yield
    logger.info(f"Completed test: {request.node.name}")

def pytest_configure(config):
    """Configure pytest"""
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test"
    )
    config.addinivalue_line(
        "markers", "api: mark test as API test"
    )

# Set environment variables directly
os.environ["BASE_URL"] = "https://d3g8su2w1x0h24.cloudfront.net"
