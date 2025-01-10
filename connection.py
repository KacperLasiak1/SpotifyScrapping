import os
import base64
from requests import post
import json

# Set the current directory
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_DIRECTORY)

# Spotify API credentials
CLIENT_ID = "XXX"
CLIENT_SECRET = "XXX"

def get_token():
    """
    Function to generate an access token for Spotify API using client credentials.
    """
    # Encode client ID and client secret
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_encoded = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_encoded), "utf-8")

    # Spotify API token URL
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

# Base URLs
SPOTIFY_BASE_URL = "https://api.spotify.com/v1"
ACCESS_TOKEN = get_token()
OSM_API_URL = "https://nominatim.openstreetmap.org/search"
