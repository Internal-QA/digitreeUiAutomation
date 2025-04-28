from config.config import BASE_URL

# Remove trailing slash from BASE_URL if present and add path
login_endpoint = f"{BASE_URL.rstrip('/')}/api/auth/user/login"
