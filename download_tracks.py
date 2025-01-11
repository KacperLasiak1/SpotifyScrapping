import connection as con
import requests
import pandas as pd

def fetch_playlist_tracks(playlist_id):
    """
    Fetches tracks from a Spotify playlist given its playlist ID.

    This function uses Spotify's API to retrieve detailed information about tracks
    in a specified playlist. It handles pagination by iteratively fetching data until
    all tracks are retrieved.

    Args:
        playlist_id (str): The Spotify playlist ID.

    Returns:
        pd.DataFrame: A pandas DataFrame containing details of each track in the playlist.

    Example:
        df = fetch_playlist_tracks('3u9PlY0zXI4pvQtJuv0OqJ')
    """
    url = f"{con.SPOTIFY_BASE_URL}/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {con.ACCESS_TOKEN}"
    }

    tracks = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            items = data.get("items", [])

            for item in items:
                track = item["track"]
                tracks.append({
                    "track_name": track["name"],
                    "artist_name": ", ".join([artist["name"] for artist in track["artists"]]),
                    "album_name": track["album"]["name"],
                    "release_date": track["album"]["release_date"],
                    "popularity": track["popularity"],
                    "track_id": track["id"],
                    "duration_ms": track["duration_ms"],
                    "explicit": track["explicit"],
                    "available_markets": len(track.get("available_markets", []))
                })

            url = data.get("next")  # URL for the next page of results
        else:
            print("Error fetching playlist data:", response.json())
            break
    
    print("Fetching tracks from playlist...")
    if tracks:
        # Convert to DataFrame and save to a file
        df = pd.DataFrame(tracks)
        print("Playlist data saved.")
    else:
        print("No tracks found.")
    
    return df
