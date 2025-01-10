import os
import base64
from requests import post
import json

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_DIRECTORY)

CLIENT_ID = "XXX"
CLIENT_SECRET = "XXX"

def get_token():
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_encoded = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_encoded), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers = headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

SPOTIFY_BASE_URL = "https://api.spotify.com/v1"
ACCESS_TOKEN = get_token()
OSM_API_URL = "https://nominatim.openstreetmap.org/search"

#Test the directory
#print(f"Working directory set to: {os.getcwd()}")
# print(client_id, client_secret)
#print(ACCESS_TOKEN)

