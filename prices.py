import pandas as pd

# Define popularity ranges and countries
popularity_ranges = ['0-50', '50-75', '75-90', '90+']
countries = ['Poland', 'Germany', 'France', 'Spain', 'Norway', 'Italy', 'United Kingdom', 'Belgium']

# Define country factors
country_factor = {
    'Poland': 1.0,
    'Germany': 0.9,
    'France': 0.85,
    'Spain': 0.8,
    'Norway': 0.95,
    'Italy': 0.9,
    'United Kingdom': 0.75,
    'Belgium': 0.8,
}

# Define popularity multipliers
popularity_multiplier = {
    '0-50': 1,
    '50-75': 1.5,
    '75-90': 5,
    '90+': 10,
}

# Create combinations of country and popularity range
combinations = [(country, prange) for country in countries for prange in popularity_ranges]

# Create DataFrame from combinations
price_data = pd.DataFrame(combinations, columns=['Country', 'Popularity Range'])

# Define base price
base_price = 15000

# Map country factors and popularity multipliers
price_data['Country Factor'] = price_data['Country'].map(country_factor)
price_data['Popularity Multiplier'] = price_data['Popularity Range'].map(popularity_multiplier)

# Calculate total price
price_data['Total Price [$]'] = base_price * price_data['Country Factor'] * price_data['Popularity Multiplier']

# Optional: Print the DataFrame to verify
# print(price_data)
