# API Endpoint Documentation Template

## Endpoint Information
- **Name**: [Endpoint Name]
- **URL**: `/api/[resource]/[id]`
- **Method**: `GET` | `POST` | `PUT` | `DELETE` | `PATCH`
- **Auth Required**: Yes | No
- **Permissions Required**: [Permissions if applicable]
- **Rate Limited**: Yes (100 requests/hour) | No

## Description
Brief description of what this endpoint does and its purpose in the system.

## URL Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | integer | Yes | Unique identifier for the [resource] |
| `include` | string | No | Comma-separated list of related resources to include |

## Query Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `page` | integer | No | 1 | Page number for paginated results |
| `limit` | integer | No | 20 | Number of items per page (max 100) |
| `sort` | string | No | `created_at` | Field to sort by |
| `order` | string | No | `desc` | Sort order (`asc` or `desc`) |
| `filter` | string | No | None | Filter expression (e.g., `status:active,type:user`) |

## Request Headers
| Header | Value | Required | Description |
|--------|-------|----------|-------------|
| `Authorization` | `Bearer {token}` | Yes | JWT authentication token |
| `Content-Type` | `application/json` | Yes | Request body format |
| `Accept` | `application/json` | No | Response format |

## Request Body
```json
{
  "name": "string",
  "email": "string",
  "role": "string",
  "active": boolean
}
```

| Field | Type | Required | Description | Constraints |
|-------|------|----------|-------------|------------|
| `name` | string | Yes | User's full name | Min 2, Max 100 chars |
| `email` | string | Yes | User's email address | Valid email format |
| `role` | string | No | User's role | One of: `admin`, `user`, `guest` |
| `active` | boolean | No | Whether user is active | Default: `true` |

## Success Response
- **Code**: `200 OK` | `201 Created` | `204 No Content`
- **Content**:
```json
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com",
  "role": "admin",
  "active": true,
  "created_at": "2023-08-15T14:30:00Z",
  "updated_at": "2023-08-15T14:30:00Z"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Unique identifier |
| `name` | string | User's full name |
| `email` | string | User's email address |
| `role` | string | User's role |
| `active` | boolean | Whether user is active |
| `created_at` | string (ISO datetime) | Creation timestamp |
| `updated_at` | string (ISO datetime) | Last update timestamp |

## Error Responses
| Status Code | Error Code | Message | Reason |
|-------------|------------|---------|--------|
| `400 Bad Request` | `INVALID_REQUEST` | Invalid request body | Request validation failed |
| `401 Unauthorized` | `AUTHENTICATION_REQUIRED` | Authentication required | Missing or invalid token |
| `403 Forbidden` | `INSUFFICIENT_PERMISSIONS` | Insufficient permissions | User lacks required permissions |
| `404 Not Found` | `RESOURCE_NOT_FOUND` | User not found | Resource with given ID doesn't exist |
| `422 Unprocessable Entity` | `VALIDATION_ERROR` | Email already exists | Unique constraint violation |
| `429 Too Many Requests` | `RATE_LIMIT_EXCEEDED` | Too many requests | Rate limit exceeded |
| `500 Internal Server Error` | `SERVER_ERROR` | Internal server error | Server-side error occurred |

## Error Response Format
```json
{
  "error": true,
  "code": "ERROR_CODE",
  "message": "Human-readable error message",
  "details": {
    "field": ["Specific error details"]
  },
  "trace_id": "request-trace-id-for-debugging"
}
```

## Sample Request
```bash
curl -X POST "https://api.example.com/api/users" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "role": "admin"
  }'
```

## Sample Response
```json
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com",
  "role": "admin",
  "active": true,
  "created_at": "2023-08-15T14:30:00Z",
  "updated_at": "2023-08-15T14:30:00Z"
}
```

## Notes
- This endpoint uses cursor-based pagination for large result sets
- Rate limiting is applied per API key, not per user
- Deleted resources are soft-deleted and will still appear with `active: false`

## Related Endpoints
- `GET /api/users` - List all users
- `GET /api/users/{id}/permissions` - Get user permissions
- `POST /api/users/{id}/reset-password` - Reset user password

## Version History
| Version | Date | Description |
|---------|------|-------------|
| v1.0 | 2023-08-01 | Initial implementation |
| v1.1 | 2023-09-15 | Added `include` parameter for related resources |
| v2.0 | 2024-01-10 | Changed response format to include `created_at` and `updated_at` |

## Implementation Examples

### FastAPI
```python
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

router = APIRouter()

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    role: Optional[str] = Field("user", pattern="^(admin|user|guest)$")
    active: Optional[bool] = True

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    active: bool
    created_at: str
    updated_at: str

@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, current_user = Depends(get_current_user)):
    # Implementation details
    pass
```

### Flask
```python
from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, validate, ValidationError

bp = Blueprint("users", __name__, url_prefix="/api")

class UserSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    email = fields.Email(required=True)
    role = fields.Str(load_default="user", validate=validate.OneOf(["admin", "user", "guest"]))
    active = fields.Bool(load_default=True)

@bp.route("/users", methods=["POST"])
@jwt_required
def create_user():
    try:
        schema = UserSchema()
        data = schema.load(request.json)
        # Implementation details
        return jsonify(response_data), 201
    except ValidationError as err:
        return jsonify({"error": True, "code": "VALIDATION_ERROR", "details": err.messages}), 400
```

### Django
```python
from rest_framework import serializers, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'role', 'active', 'created_at', 'updated_at']
        extra_kwargs = {
            'name': {'min_length': 2, 'max_length': 100},
            'role': {'default': 'user'}
        }

    def validate_role(self, value):
        if value not in ['admin', 'user', 'guest']:
            raise serializers.ValidationError("Role must be one of: admin, user, guest")
        return value

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Implementation details
        return Response(serializer.data, status=status.HTTP_201_CREATED)
``` 