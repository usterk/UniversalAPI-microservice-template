"""Unit tests for health endpoint."""

from app.version import VERSION


def test_health_returns_200(client):
    """Health endpoint should return 200 OK."""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_healthy_status(client):
    """Health endpoint should return healthy status."""
    response = client.get("/health")
    data = response.json()
    assert data["status"] == "healthy"


def test_health_returns_version(client):
    """Health endpoint should return current version."""
    response = client.get("/health")
    data = response.json()
    assert "version" in data
    assert data["version"] == VERSION


def test_health_returns_app_name(client):
    """Health endpoint should return app name."""
    response = client.get("/health")
    data = response.json()
    assert "app_name" in data
