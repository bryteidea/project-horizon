# config Directory

This directory contains configuration files for different environments (development, testing, staging, production). It centralizes all configuration to make environment-specific settings easy to manage.

## Common Files

```
config/
├─ .env.example           # Template for environment variables (NEVER commit actual .env files)
├─ development.yaml       # Development environment settings
├─ testing.yaml           # Test environment settings
├─ production.yaml        # Production environment settings
├─ docker-compose.yml     # Docker configuration
├─ docker-compose.dev.yml # Development-specific Docker overrides
└─ logging.yaml           # Logging configuration
```

## Environment Variables (.env.example)

```
# Database settings
DB_HOST=localhost
DB_PORT=5432
DB_NAME=myapp
DB_USER=postgres
DB_PASSWORD=example_password  # Use placeholder in .env.example

# API settings
API_PORT=8000
API_DEBUG=true
API_SECRET_KEY=example_secret_key  # Use placeholder in .env.example

# Third-party services
MAILGUN_API_KEY=example_key
S3_BUCKET=mybucket
```

## Configuration YAML Example

```yaml
# development.yaml
app:
  name: "MyApp"
  debug: true
  host: "0.0.0.0"
  port: 8000
  
database:
  dialect: "postgresql"
  pool_size: 10
  timeout: 30
  
security:
  jwt_expiration: 86400  # 24 hours in seconds
  password_reset_timeout: 3600  # 1 hour
  
features:
  enable_registration: true
  allow_social_login: true
  rate_limit: 100  # requests per minute
```

## Loading Configuration

```python
# src/config.py
import os
import yaml
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Determine environment
ENV = os.getenv("ENVIRONMENT", "development")

# Load YAML config
with open(f"config/{ENV}.yaml", "r") as f:
    config = yaml.safe_load(f)

# Example usage
DEBUG = config["app"]["debug"]
DB_URI = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
```

## Best Practices

1. Never commit sensitive information (.env files, API keys, passwords)
2. Use environment variables for secrets, YAML for structural configuration
3. Include validation for required configuration values
4. Document all configuration options

Made with love by Bryte Idea
