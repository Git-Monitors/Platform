import os

from fastapi.exceptions import HTTPException


def check_environment():
    REQUIRED_ENV_VARS = [
        'DISCORD_CLIENT_ID',
        'DISCORD_AUTH_REDIRECT_URL',
        'DISCORD_AUTH_ROOT_URL',
        'DISCORD_AUTH_SCOPE',
        'DISCORD_AUTH_RESPONSE_TYPE',
        'DISCORD_CLIENT_SECRET'
    ]

    for var in REQUIRED_ENV_VARS:
        if not os.getenv(var):
            raise HTTPException(
                status_code=500, detail=f"Missing environment variable {var}")
