import download_tracks as dt
import market_playlists as mp
import pandas as pd
import numpy as np
from prices import price_data


def country_analysis(chosen_country, explicit = False):
    playlist_id = mp.playlist_data.loc[mp.playlist_data['country'] == chosen_country, 'playlist_id'].iloc[0]
    track_list = dt.fetch_playlist_tracks(playlist_id)

    if explicit == False:
        track_list = track_list[track_list['explicit'] != "True"]

    #most frequent artists and their average popularity
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

    artists.to_csv("artists", index=False)

    return artists


def calculate_prices(price_data = price_data):
    country = input("Enter Country: ")
    explicit_choice = input("Do you want to include explicit artists? [Y/N]: ")
    if explicit_choice == "Y":
        explicit = True
    else:
        explicit = False

    artists = country_analysis(country, explicit)

    price_data = price_data[price_data['Country'] == country]
    artists = artists.merge(price_data[['Popularity Range', 'Total Price [$]']], left_on='average_popularity_class',
                            right_on='Popularity Range', how='left')
    artists.drop(columns=['Popularity Range'], inplace=True)
    artists['Total Price [$]'] = artists['Total Price [$]'].astype(int)
    return artists

