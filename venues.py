import googlemaps

API_KEY = 'XXX'

def get_concert_venues(country_name, api_key):
    """
    Retrieves concert venues in a specified country using Google Maps API.

    This function initializes the Google Maps client with the provided API key,
    searches for concert venues in the given country, and extracts their names and addresses.

    Args:
        country_name (str): The name of the country where concert venues are searched.
        api_key (str): The Google Maps API key.

    Returns:
        list[dict]: A list of dictionaries containing venue names and addresses.

    Example:
        venues = get_concert_venues('United States', API_KEY)
    """
    # Initialize the Google Maps client
    gmaps = googlemaps.Client(key=api_key)

    # Search for concert venues in the specified country
    places_result = gmaps.places(
        query="concert",
        location=None,
        region=country_name
    )

    selected_venues = []
    # Extract and display venue names and addresses
    if places_result.get('results'):
        for venue in places_result['results']:
            name = venue.get('name', 'Unknown Name')
            address = venue.get('formatted_address', 'Unknown Address')
            selected_venues.append({
                'venue_name': name,
                'venue_address': address
            })
    return selected_venues
