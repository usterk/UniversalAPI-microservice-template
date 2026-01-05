"""End-to-end tests for API endpoints."""


def test_root_endpoint(client):
    """Root endpoint should return API info."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "endpoints" in data
    assert "/health" in data["endpoints"]
    assert "/ip" in data["endpoints"]
    assert "/headers" in data["endpoints"]


def test_ip_endpoint(client):
    """IP endpoint should return client IP info."""
    response = client.get("/ip")
    assert response.status_code == 200
    data = response.json()
    assert "ip" in data
    assert "forwarded_for" in data
    assert "real_ip" in data
    assert "host" in data
    assert "user_agent" in data


def test_ip_endpoint_with_forwarded_header(client):
    """IP endpoint should respect X-Forwarded-For header."""
    response = client.get("/ip", headers={"X-Forwarded-For": "1.2.3.4, 5.6.7.8"})
    assert response.status_code == 200
    data = response.json()
    assert data["ip"] == "1.2.3.4"
    assert data["forwarded_for"] == "1.2.3.4, 5.6.7.8"


def test_headers_endpoint(client):
    """Headers endpoint should return all request headers."""
    response = client.get("/headers", headers={"X-Custom-Header": "test-value"})
    assert response.status_code == 200
    data = response.json()
    assert "x-custom-header" in data
    assert data["x-custom-header"] == "test-value"


def test_full_flow(client):
    """Test complete API flow."""
    # Check health
    health = client.get("/health")
    assert health.status_code == 200
    assert health.json()["status"] == "healthy"

    # Get root info
    root = client.get("/")
    assert root.status_code == 200

    # Get IP info
    ip_info = client.get("/ip")
    assert ip_info.status_code == 200

    # Get headers
    headers = client.get("/headers")
    assert headers.status_code == 200
