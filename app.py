from tracks_analysis import calculate_prices
from artist_booking import booking
import venues


if __name__ == "__main__":
    artists = calculate_prices()
    selected_artists = booking(artists)
    country_venues = input("Enter the code of the country to find popular concert venues: ")
    venues.get_concert_venues(country_venues, venues.API_KEY)