import download_tracks as dt
import market_playlists as mp
import pandas as pd
import numpy as np
from prices import price_data

def country_analysis(chosen_country, explicit=False):
    """
    Function to analyze a country's music playlist and calculate artist statistics.

    Parameters:
    - chosen_country (str): The country for which the analysis is performed.
    - explicit (bool): Flag to include explicit tracks (default: False).

    Returns:
    - artists (DataFrame): DataFrame containing artist analysis with average popularity and occurrence.
    """
    # Get playlist ID for the chosen country
    playlist_id = mp.playlist_data.loc[mp.playlist_data['country'] == chosen_country, 'playlist_id'].iloc[0]

    # Fetch playlist tracks
    track_list = dt.fetch_playlist_tracks(playlist_id)

    # Filter explicit tracks if required
    if not explicit:
        track_list = track_list[track_list['explicit'] != "True"]

    # Split and explode artist names for frequency and popularity analysis
    track_list['artist_name'] = track_list['artist_name'].str.split(', ')
    track_list = track_list.explode('artist_name')

    # Count artist occurrences
    artist_counts = track_list['artist_name'].value_counts().reset_index()
    artist_counts.columns = ['artist_name', 'occurences']

    # Calculate average popularity per artist
    average_popularity = track_list.groupby('artist_name')['popularity'].mean().reset_index()
    average_popularity.columns = ['artist_name', 'average_popularity']
    average_popularity['average_popularity'] = average_popularity['average_popularity'].round(2)

    # Merge counts and average popularity
    artists = pd.merge(artist_counts, average_popularity, on='artist_name')

    # Classify average popularity into ranges
    if artists['average_popularity'].dtype in [int, float]:
        conditions = [
            artists['average_popularity'] <= 50,
            artists['average_popularity'] <= 75,
            artists['average_popularity'] <= 90
        ]
        choices = ['0-50', '50-75', '75-90']
        artists['average_popularity_class'] = np.select(conditions, choices, default='90+')

    # Save artist data to a CSV file
    artists.to_csv("artists.csv", index=False)

    return artists

def calculate_prices(price_data=price_data):
    """
    Function to calculate the price of artists based on country and popularity class.

    Parameters:
    - price_data (DataFrame): Predefined price data (default: from prices module).

    Returns:
    - artists (DataFrame): DataFrame containing artist data along with calculated prices.
    """
    # User input for country and explicit track inclusion
    country = input("Enter Country: ")
    explicit_choice = input("Do you want to include explicit artists? [Y/N]: ")

    explicit = True if explicit_choice.upper() == "Y" else False

    # Analyze the country and get artist data
    artists = country_analysis(country, explicit)

    # Filter price data for the chosen country
    price_data = price_data[price_data['Country'] == country]

    # Merge artist data with price data
    artists = artists.merge(price_data[['Popularity Range', 'Total Price [$]']], left_on='average_popularity_class',
                            right_on='Popularity Range', how='left')

    # Clean up the dataframe
    artists.drop(columns=['Popularity Range'], inplace=True)
    artists['Total Price [$]'] = artists['Total Price [$]'].astype(int)

    return artists
