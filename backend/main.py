from dotenv import load_dotenv
from fastapi import FastAPI
from middlewares.errors import error_parser  

from routes.discord_login import router as discord_login_router

load_dotenv()


app = FastAPI()
app.include_router(discord_login_router, prefix="/discord")

# Simple health check endpoint
@app.get("/")
def health():
    return {"message": "Auth server running"}


# Any exception in server is caught here
@app.exception_handler(Exception)
async def exception_handler(request, exc):
    return await error_parser(request, exc)
