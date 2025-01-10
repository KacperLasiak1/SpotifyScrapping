def booking(artists):
    budget = int(input("Specify your budget: "))
    number_of_artists = int(input("Specify number of artists: "))
    sorted_artists = artists.sort_values(by='Total Price [$]', ascending = False)

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
            print(f"Your budget is too small to book {number_of_artists} artists...")
            selected_artists.clear()
            break

        if len(selected_artists) == number_of_artists:
            total_price = sum(artist['total_price'] for artist in selected_artists)
            print("Selected artists:")
            for artist in selected_artists:
                print(f"Artist Name: {artist['artist_name']}, Total Price: {artist['total_price']}")
            print(f"Total Price of Selected Artists: {total_price}")

    return selected_artists


