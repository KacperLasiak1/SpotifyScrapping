import googlemaps

# Replace 'XXX' with your actual API key
API_KEY = 'XXX'

def get_concert_venues(country_name, api_key):
    """
    Function to retrieve concert venues in a specified country using Google Maps API.

    Parameters:
    - country_name (str): Name of the country to search for concert venues.
    - api_key (str): API key for Google Maps API.

    Returns:
    - None: Prints venue names and addresses.
    """
    # Initialize the Google Maps client
    gmaps = googlemaps.Client(key=api_key)

    # Search for concert venues in the specified country
    places_result = gmaps.places(
        query="concert",
        location=None,
        region=country_name
    )

    # Extract and display venue names and addresses
    if places_result.get('results'):
        print(f"Popular concert venues in {country_name}:")
        for venue in places_result['results']:
            name = venue.get('name', 'Unknown Name')
            address = venue.get('formatted_address', 'Unknown Address')
            print(f"- {name}, located at {address}")
    else:
        print(f"No concert venues found in {country_name}.")
