import download_tracks as dt
import market_playlists as mp
import pandas as pd
import numpy as np
from prices import price_data

def country_analysis(chosen_country, explicit=False):
    """
    Analyzes tracks in a Spotify playlist for a chosen country.

    This function retrieves the playlist ID for a specified country, fetches track data from that playlist,
    and provides analysis of artists, including their frequency and average popularity. If `explicit` is set to
    `False`, tracks marked as explicit are excluded from the analysis.

    Args:
        chosen_country (str): The country for which to analyze the playlist.
        explicit (bool): Whether to exclude explicit tracks from the analysis. Default is False.

    Returns:
        pd.DataFrame: A DataFrame with artists, their occurrences, and average popularity. Additionally,
                      the popularity class (e.g., '0-50', '50-75') is included.

    Example:
        artists_df = country_analysis('USA', explicit=True)
    """
    playlist_id = mp.playlist_data.loc[mp.playlist_data['country'] == chosen_country, 'playlist_id'].iloc[0]
    track_list = dt.fetch_playlist_tracks(playlist_id)

    if explicit == False:
        track_list = track_list[track_list['explicit'] != "True"]

    # Most frequent artists and their average popularity
    track_list['artist_name'] = track_list['artist_name'].str.split(', ')
    track_list = track_list.explode('artist_name')

    artist_counts = track_list['artist_name'].value_counts().reset_index()
    artist_counts.columns = ['artist_name', 'occurences']

    average_popularity = track_list.groupby('artist_name')['popularity'].mean().reset_index()
    average_popularity.columns = ['artist_name', 'average_popularity']
    average_popularity['average_popularity'] = average_popularity['average_popularity'].round(2)

    artists = pd.merge(artist_counts, average_popularity, on='artist_name')

    if artists['average_popularity'].dtype in [int, float]:
        conditions = [
            artists['average_popularity'] <= 50,
            artists['average_popularity'] <= 75,
            artists['average_popularity'] <= 90
        ]
        choices = ['0-50', '50-75', '75-90']
        artists['average_popularity_class'] = np.select(conditions, choices, default='90+')

    return artists


def calculate_prices(artists, country, price_data=price_data):
    """
    Calculates the total price for artists based on their popularity class.

    This function merges the artist DataFrame with price data based on the popularity class, and 
    ensures that the appropriate price is assigned to each artist. 

    Args:
        artists (pd.DataFrame): The DataFrame containing artist data with average popularity.
        country (str): The country for which to calculate prices.
        price_data (pd.DataFrame): The price data mapping popularity ranges to prices. Default is imported `price_data`.

    Returns:
        pd.DataFrame: A DataFrame with artist names, their popularity class, and calculated total prices.

    Example:
        priced_artists_df = calculate_prices(artists_df, 'USA')
    """
    price_data = price_data[price_data['Country'] == country]
    artists = artists.merge(price_data[['Popularity Range', 'Total Price [$]']], left_on='average_popularity_class',
                            right_on='Popularity Range', how='left')
    artists.drop(columns=['Popularity Range'], inplace=True)
    artists['Total Price [$]'] = artists['Total Price [$]'].astype(int)
    return artists
