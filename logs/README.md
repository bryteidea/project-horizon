# logs Directory

This directory stores application logs that are useful for debugging, monitoring, and auditing. Logs should NOT be committed to Git (they are in .gitignore).

## Log Files

Typical log files found here:

```
logs/
├─ app.log                 # Main application logs
├─ error.log               # Error-level logs only
├─ access.log              # HTTP request logs (for web apps)
├─ background_tasks.log    # Background job logs
├─ db_queries.log          # Database query logs (in development)
└─ archives/               # Archived/rotated logs
   ├─ app.log.1
   ├─ app.log.2
```

## Log Format

Logs should follow a consistent format:

```
2025-04-30 14:23:12,543 [INFO] user_service: User 'john.doe' logged in successfully - ip=192.168.1.1
2025-04-30 14:25:07,891 [ERROR] payment_service: Payment failed - user_id=123 amount=59.99 error="Insufficient funds"
```

## Log Configuration

Logging is configured in `src/config.py`. Example configuration:

```python
import logging
import os

def setup_logging():
    """Configure application logging."""
    log_format = '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    
    # Configure root logger
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.INFO,
        format=log_format,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Configure error logger
    error_handler = logging.FileHandler('logs/error.log')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter(log_format))
    logging.getLogger().addHandler(error_handler)
```

## Log Rotation

Logs are automatically rotated (using the standard logging.handlers.RotatingFileHandler):
- When files reach 10MB
- Keeping 5 backup files

## Notes

1. Don't use logs for sensitive information (passwords, tokens, etc.)
2. Use appropriate log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
3. Include context in log messages (user IDs, request IDs, etc.)

Made with love by Bryte Idea
