import pandas as pd

# Playlist IDs for top charts in different countries
top_pl = "4uaEDs7NwMGTJAYCFI5zEf"
top_de = "1GY1Shfb5S0OEKkV0azlG2"
top_fr = "07QOxquGiEKaQO6Z2YIbeC"
top_esp = "4YWzZ8BVCpJ1MVo8D3K6D3"
top_nor = "5ezCvZuFJcmMUeOynIYp6g"
top_it = "0kfNtsIwTOayAy7MaSaEyK"
top_uk = "4L5OntrMDtos3KrFgfy83S"
top_bel = "0BOIbwftVstsNHSpwLVZs0"

# Create a DataFrame for playlist data
playlist_data = pd.DataFrame([
    {"id": "top_pl", "country": "Poland", "playlist_id": top_pl},
    {"id": "top_de", "country": "Germany", "playlist_id": top_de},
    {"id": "top_fr", "country": "France", "playlist_id": top_fr},
    {"id": "top_esp", "country": "Spain", "playlist_id": top_esp},
    {"id": "top_nor", "country": "Norway", "playlist_id": top_nor},
    {"id": "top_it", "country": "Italy", "playlist_id": top_it},
    {"id": "top_uk", "country": "United Kingdom", "playlist_id": top_uk},
    {"id": "top_bel", "country": "Belgium", "playlist_id": top_bel}
])

