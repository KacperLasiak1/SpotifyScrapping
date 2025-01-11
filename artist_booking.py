def booking(artists, budget, number_of_artists):
    """
    Selects artists for booking based on a given budget and the number of artists required.

    The function sorts the input DataFrame of artists by their "Total Price [$]" in descending order.
    It selects artists whose prices fit within the remaining budget until the desired number of artists
    is reached or the list of available artists is exhausted. If the budget is insufficient to book
    the required number of artists, a message is added to the result.

    Args:
        artists (pd.DataFrame): A pandas DataFrame containing artist data, including "Total Price [$]" and "artist_name".
        budget (float): The total budget available for booking artists.
        number_of_artists (int): The desired number of artists to book.

    Returns:
        list[dict]: A list of dictionaries, each containing:
            - 'artist_name' (str): The name of the artist.
            - 'total_price' (int): The price of the artist.
        If the budget is insufficient, a single dictionary with a message is returned.

    Example:
        Input:
            artists = pd.DataFrame({
                'artist_name': ['Artist A', 'Artist B', 'Artist C'],
                'Total Price [$]': [1000, 2000, 1500]
            })
            budget = 2500
            number_of_artists = 2

        Output:
            [
                {'artist_name': 'Artist B', 'total_price': 2000},
                {'artist_name': f"Your budget is too small to book 2 artists...", 'total_price': 0}
            ]
    """
    sorted_artists = artists.sort_values(by='Total Price [$]', ascending=False)
    selected_artists = []
    remaining_budget = budget

    while len(selected_artists) < number_of_artists and not sorted_artists.empty:
        if sorted_artists.iloc[0]['Total Price [$]'] <= remaining_budget:
            selected_artists.append({
                'artist_name': sorted_artists.iloc[0]['artist_name'],
                'total_price': int(sorted_artists.iloc[0]['Total Price [$]'])
            })
            remaining_budget -= sorted_artists.iloc[0]['Total Price [$]']
            sorted_artists = sorted_artists.drop(sorted_artists.index[0])
        else:
            sorted_artists = sorted_artists.drop(sorted_artists.index[0])

        if sorted_artists.empty:
            selected_artists.append({'artist_name': f"Your budget is too small to book {number_of_artists} artists...",
                                     'total_price': 0})
            break

    return selected_artists
