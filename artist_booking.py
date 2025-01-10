def booking(artists):
    """
    Function to select a specified number of artists within a given budget.
    
    Parameters:
    - artists (DataFrame): A DataFrame containing artist information with columns 'artist_name' and 'Total Price [$]'.

    Returns:
    - selected_artists (list): A list of dictionaries with selected artist names and their corresponding total prices.
    """

    # Request budget from the user
    budget = int(input("Specify your budget: "))

    # Request the number of artists to be booked
    number_of_artists = int(input("Specify number of artists: "))

    # Sort artists by total price in descending order
    sorted_artists = artists.sort_values(by='Total Price [$]', ascending=False)

    selected_artists = []  # List to store selected artists
    remaining_budget = budget  # Remaining budget after selecting artists

    while len(selected_artists) < number_of_artists and not sorted_artists.empty:
        # Check if the top artist can be booked within the remaining budget
        if sorted_artists.iloc[0]['Total Price [$]'] <= remaining_budget:
            # Add artist to selected list
            selected_artists.append({
                'artist_name': sorted_artists.iloc[0]['artist_name'],
                'total_price': int(sorted_artists.iloc[0]['Total Price [$]'])
            })
            # Update the remaining budget
            remaining_budget -= sorted_artists.iloc[0]['Total Price [$]']
            # Remove the selected artist from the sorted list
            sorted_artists = sorted_artists.drop(sorted_artists.index[0])
        else:
            # If the artist exceeds budget, remove them
            sorted_artists = sorted_artists.drop(sorted_artists.index[0])

        # Break the loop if no artists are left to select
        if sorted_artists.empty:
            print(f"Your budget is too small to book {number_of_artists} artists...")
            selected_artists.clear()
            break

        # Check if the required number of artists has been selected
        if len(selected_artists) == number_of_artists:
            # Calculate the total price of selected artists
            total_price = sum(artist['total_price'] for artist in selected_artists)
            print("Selected artists:")
            for artist in selected_artists:
                print(f"Artist Name: {artist['artist_name']}, Total Price: {artist['total_price']}")
            print(f"Total Price of Selected Artists: {total_price}")

    return selected_artists
