from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
  

async def error_parser(request: Request, exception: Exception):
    status_code = 500
    message = str(exception)
    if isinstance(exception, HTTPException):  # conditional handling of exceptions
        status_code = exception.status_code
        message = exception.detail
    return JSONResponse(status_code=status_code, content={"message": message})  # send an error respnse instead of crashing the server