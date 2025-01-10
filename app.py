from tracks_analysis import calculate_prices
from artist_booking import booking
import venues

# Main execution block
if __name__ == "__main__":
    # Step 1: Calculate prices for artists
    artists = calculate_prices()

    # Step 2: Book selected artists
    selected_artists = booking(artists)

    # Step 3: Get popular concert venues for a chosen country
    country_venues = input("Enter the code of the country to find popular concert venues: ")
    venues.get_concert_venues(country_venues, venues.API_KEY)
