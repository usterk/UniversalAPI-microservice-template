FROM nginx:alpine

# Copy static files
COPY src/ /usr/share/nginx/html/

# Health check endpoint (returns 200 for index.html)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget -q --spider http://127.0.0.1:80/ || exit 1

EXPOSE 80
