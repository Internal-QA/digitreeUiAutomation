# Valuation test data
valid_valuation_payload = {
    "dealer_info_id": 21739,
    "name": "Estimate_22 Apr 2025 12:15:17",
    "config_id": 1421,
    "isInstantReport": True,
    "dealer_id": "52"
}

# Valuation test cases
INVALID_DEALER_ID = "99999"
INVALID_CONFIG_ID = 9999
MISSING_REQUIRED_FIELDS = {
    "dealer_info_id": 21739,
    "name": "Test Valuation"
} 