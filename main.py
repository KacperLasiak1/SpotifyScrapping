import tkinter as tk
from tkinter import ttk
from tracks_analysis import calculate_prices, country_analysis
from artist_booking import booking
from prices import price_data
from venues import get_concert_venues, API_KEY

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x600')
        self.root.title('Music Event Planner')

        # Main frame setup
        self.mainframe = tk.Frame(self.root, background='#f7f7f7', padx=20, pady=20)
        self.mainframe.pack(fill='both', expand=True)

        # Title
        ttk.Label(
            self.mainframe, text="Welcome to Music Event Planner!",
            background='#f7f7f7', font=("Helvetica", 18, "bold"), anchor="center"
        ).grid(row=0, column=0, columnspan=2, pady=10)

        # Country selection
        ttk.Label(self.mainframe, text="Select Country:", background='#f7f7f7', font=("Helvetica", 12)).grid(row=1, column=0, sticky='w', pady=5)

        country_options = ['Poland', 'Germany', 'France', 'Spain', 'Norway', 'Italy', 'United Kingdom', 'Belgium']
        self.set_country_field = ttk.Combobox(self.mainframe, values=country_options, state="readonly")
        self.set_country_field.grid(row=1, column=1, pady=5, sticky='ew')

        # Explicit content selection
        ttk.Label(self.mainframe, text="Allow Explicit Content:", background='#f7f7f7', font=("Helvetica", 12)).grid(row=2, column=0, sticky='w', pady=5)

        explicit_options = ['Yes', 'No']
        self.set_explicit_field = ttk.Combobox(self.mainframe, values=explicit_options, state="readonly")
        self.set_explicit_field.grid(row=2, column=1, pady=5, sticky='ew')

        # Budget input
        ttk.Label(self.mainframe, text="Enter Budget ($):", background='#f7f7f7', font=("Helvetica", 12)).grid(row=3, column=0, sticky='w', pady=5)

        self.set_budget_field = ttk.Entry(self.mainframe)
        self.set_budget_field.grid(row=3, column=1, pady=5, sticky='ew')

        # Number of artists
        ttk.Label(self.mainframe, text="Number of Artists:", background='#f7f7f7', font=("Helvetica", 12)).grid(row=4, column=0, sticky='w', pady=5)

        self.set_no_of_artists_field = ttk.Entry(self.mainframe)
        self.set_no_of_artists_field.grid(row=4, column=1, pady=5, sticky='ew')

        # Accept button for artist selection
        ttk.Button(self.mainframe, text="Choose Artists", command=self.choose_artists).grid(row=5, column=0, columnspan=2, pady=10)

        # Selected artists and price display
        self.chosen_artists = ttk.Label(self.mainframe, text="", background='#f7f7f7', font=("Helvetica", 10), wraplength=400, justify="left")
        self.chosen_artists.grid(row=6, column=0, columnspan=2, pady=5)

        self.total_price = ttk.Label(self.mainframe, text="", background='#f7f7f7', font=("Helvetica", 10))
        self.total_price.grid(row=7, column=0, columnspan=2, pady=5)

        # Country code for venue selection
        ttk.Label(self.mainframe, text="Select Country Code for Venues:", background='#f7f7f7', font=("Helvetica", 12)).grid(row=8, column=0, sticky='w', pady=5)

        country_code_options = ['PL', 'DE', 'FR', 'ES', 'NO', 'IT', 'GB', 'BE']
        self.country_code_field = ttk.Combobox(self.mainframe, values=country_code_options, state="readonly")
        self.country_code_field.grid(row=8, column=1, pady=5, sticky='ew')

        # Accept button for venue selection
        ttk.Button(self.mainframe, text="Choose Venues", command=self.choose_venues).grid(row=9, column=0, columnspan=2, pady=10)

        # Selected venues display
        self.chosen_venues = ttk.Label(self.mainframe, text="", background='#f7f7f7', font=("Helvetica", 10), wraplength=400, justify="left")
        self.chosen_venues.grid(row=10, column=0, columnspan=2, pady=5)

        self.root.mainloop()

    def choose_artists(self):
        country_name = self.set_country_field.get()
        budget = int(self.set_budget_field.get())
        no_of_artists = int(self.set_no_of_artists_field.get())
        explicit = self.set_explicit_field.get() == "Yes"

        artists = country_analysis(country_name, explicit)
        artists = calculate_prices(artists=artists, country=country_name)
        selected_artists = booking(artists, budget, no_of_artists)

        selected_artists_message = "Selected Artists:\n" + ", ".join([artist['artist_name'] for artist in selected_artists])
        total_price = sum(int(artist['total_price']) for artist in selected_artists)

        self.chosen_artists.config(text=selected_artists_message)
        self.total_price.config(text=f"Total Price: ${total_price}")

    def choose_venues(self):
        country_code = self.country_code_field.get()
        selected_venues = get_concert_venues(country_code, API_KEY)

        selected_venues_message = "Possible Venues:\n" + "\n".join([venue['venue_name'] for venue in selected_venues])
        self.chosen_venues.config(text=selected_venues_message)

if __name__ == '__main__':
    App()
