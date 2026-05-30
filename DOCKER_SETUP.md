# Docker Setup Guide

This document explains how to run the weather API using Docker.

## Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed (optional but recommended)

## Quick Start

### Option 1: Using Docker Compose (Recommended)

This runs both the API and Web Server services:

```bash
# Build and start all services
docker-compose up --build

# Run in detached mode (background)
docker-compose up -d --build

# Stop services
docker-compose down
```

The services will be available at:
- **API**: http://localhost:5000/api/weather?city=London
- **Web Server**: http://localhost:5001/

### Option 2: Using Docker Directly

#### Build the image:
```bash
docker build -t weather-api .
```

#### Run API service:
```bash
docker run -p 5000:5000 weather-api python api.py
```

#### Run Web Server service:
```bash
docker run -p 5001:5001 weather-api python server.py
```

## Usage Examples

### Using Docker Compose

Start both services:
```bash
docker-compose up
```

View logs:
```bash
docker-compose logs -f api
docker-compose logs -f server
```

Restart a specific service:
```bash
docker-compose restart api
```

### Using Docker Run

Get weather for a city:
```bash
curl "http://localhost:5000/api/weather?city=London"
```

### Environment Variables

You can override environment variables when running containers:

```bash
docker run -e FLASK_ENV=development -p 5000:5000 weather-api python api.py
```

## Production Considerations

For production deployment:

1. **Remove debug mode**: Update `api.py` and `server.py` to use `debug=False`
2. **Use environment variables**: Store API keys in environment variables, not in code
3. **Use a production WSGI server**: Replace Flask's development server with Gunicorn or uWSGI
4. **Add health checks**: Implement `/health` endpoints for monitoring

Example with Gunicorn:
```dockerfile
RUN pip install gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "api:app"]
```

## Troubleshooting

### Container exits immediately
- Check logs: `docker logs <container_id>`
- Verify the command is correct: `docker-compose logs`

### Port already in use
- Change the port mapping in `docker-compose.yml`: `"5002:5000"`
- Or stop other services using those ports

### Building takes too long
- The image is cached. Use `docker-compose build --no-cache` to rebuild from scratch

## File Structure

```
weather-api/
├── Dockerfile           # Container image configuration
├── docker-compose.yml   # Multi-container orchestration
├── .dockerignore        # Files to exclude from image
├── api.py              # Main API service
├── server.py           # Web server service
├── requirements.txt    # Python dependencies
├── test.py            # Tests
└── templates/         # HTML templates
```
