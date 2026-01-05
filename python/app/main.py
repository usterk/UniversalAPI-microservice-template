from fastapi import FastAPI, Request

from app.config import settings
from app.version import VERSION

app = FastAPI(
    title=settings.app_name,
    description="IP Info API - returns information about client IP and request headers",
    version=VERSION,
    root_path=settings.root_path,
)


@app.get("/health")
def health():
    """Health check endpoint with version info."""
    return {
        "status": "healthy",
        "version": VERSION,
        "app_name": settings.app_name,
    }


@app.get("/")
def root():
    """Root endpoint with API info."""
    return {
        "message": "IP Info API",
        "version": VERSION,
        "endpoints": ["/health", "/ip", "/headers"],
    }


@app.get("/ip")
def get_ip(request: Request):
    """Returns information about client IP address."""
    # Priority: CF-Connecting-IP (Cloudflare) > X-Forwarded-For > X-Real-IP > client.host
    cf_ip = request.headers.get("CF-Connecting-IP")
    forwarded_for = request.headers.get("X-Forwarded-For")
    real_ip = request.headers.get("X-Real-IP")
    client_ip = request.client.host if request.client else None

    # Determine the most reliable IP
    ip = cf_ip or (forwarded_for.split(",")[0].strip() if forwarded_for else None) or real_ip or client_ip

    return {
        "ip": ip,
        "cf_connecting_ip": cf_ip,
        "forwarded_for": forwarded_for,
        "real_ip": real_ip,
        "host": request.headers.get("Host"),
        "user_agent": request.headers.get("User-Agent"),
    }


@app.get("/headers")
def get_headers(request: Request):
    """Returns all request headers."""
    return dict(request.headers)
