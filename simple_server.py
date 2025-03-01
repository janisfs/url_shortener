"""URL Shortener FastAPI application.

This module implements a URL shortening service using FastAPI framework.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Handle root endpoint request.

    Returns:
        dict: A welcome message dictionary
    """
    return {"message": "Привет, это мой сервер!"}
