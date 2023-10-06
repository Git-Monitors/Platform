import os

import requests
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.responses import RedirectResponse
from middlewares.discord import check_environment

router = APIRouter()


@router.get("/login")
async def login_discord():
    check_environment()
    redirect_uri = f"{os.getenv('DISCORD_AUTH_ROOT_URL')}/authorize?response_type={os.getenv('DISCORD_AUTH_RESPONSE_TYPE')}&client_id={os.getenv('DISCORD_CLIENT_ID')}&scope={os.getenv('DISCORD_AUTH_SCOPE')}&redirect_uri={os.getenv('DISCORD_AUTH_REDIRECT_URL')}"
    return RedirectResponse(redirect_uri)


@router.get("/callback")
async def callback(code: str):
    check_environment()
    resp = requests.post(
        "https://discord.com/api/oauth2/token",
        data={
            "client_id": os.getenv("DISCORD_CLIENT_ID"),
            "client_secret": os.getenv("DISCORD_CLIENT_SECRET"),
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": os.getenv("DISCORD_AUTH_REDIRECT_URL"),
            "scope": "identify",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.json())
    return resp.json()
