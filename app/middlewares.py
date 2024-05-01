from typing import Annotated
from fastapi import status, HTTPException, Security
from fastapi.security import APIKeyHeader
from fastapi import Depends
from app.config import config


allowed_x_api_keys = config.get("ALLOWED_X_API_KEYS", ",").split(",")
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


def require_x_api_key(api_key_header: str = Security(api_key_header)):
    """Checks if requests header has `x-api-key` value."""
    if api_key_header not in allowed_x_api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Forbidden"
        )
    return api_key_header


RequireXAPIKeyDepedency = Annotated[str, Depends(require_x_api_key)]
