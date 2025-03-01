"""URL Shortener FastAPI application.
This module implements a URL shortening service using FastAPI framework.
"""


import random
import string
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

app = FastAPI()
url_database = {}


def generate_short_id():
    """Generate a random short ID for URL."""
    characters = string.ascii_letters + string.digits
    short_id = ''.join(random.choice(characters) for _ in range(6))
    return short_id


@app.post("/", status_code=201)
def shorten_url(url: str):
    """Create a shortened version of the provided URL.
    Args:
        url (str): Original URL to be shortened
    Returns:
        dict: Dictionary containing original and shortened URLs
    """
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    short_id = generate_short_id()
    url_database[short_id] = url
    return {"short_url": f"http://127.0.0.1:8000/{short_id}"}


@app.get("/{short_id}")
def redirect_to_url(short_id: str):
    """Redirect to original URL using provided short ID.
    Args:
        short_id (str): Short ID to look up original URL
    """
    if short_id in url_database:
        original_url = url_database[short_id]
        return RedirectResponse(url=original_url, status_code=307)
    else:
        raise HTTPException(status_code=404, detail="Short URL not found")
