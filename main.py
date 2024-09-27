from time import sleep
import csv  # Dodaj ten import

from CarListing import CarListing
from Discord import DiscordWebhookSender
from Listing import Listing
from OlxList import OlxList

if __name__ == "__main__":

    olx_url = 'https://www.olx.pl/motoryzacja/samochody/audi/?search%5Bfilter_enum_model%5D%5B0%5D=a6&search%5Bfilter_float_year:from%5D=2018&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan'

    for i in range(1,2):
        listings = OlxList.get_olx_listings(olx_url, i)
        car_listings = []
        for listing in listings:
            ad = CarListing(listing)
            car_listings.append(ad)  # Dodaj obiekt do listy
        csv_headers = [
            'title',
            'image_url',
            'location',
            'url',
            'price',
            'description',
            'vin',
            'model',
            'year',
            'petrol',
            'car_body',
            'mileage',
            'color',
            'engine_size',
            'condition',
            'transmission',
            'country_origin',
            'engine_power',
            'drive'
        ]

        # Zapisujemy dane do pliku CSV
        with open('car_listings1.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
            writer.writeheader()

            for listing in car_listings:
                row = {
                    'title': listing.title,
                    'image_url': listing.image_url,
                    'location': listing.location,
                    'url': listing.url,
                    'price': listing.price,
                    'description': listing.description,
                    'vin': getattr(listing, 'vin', ''),
                    'model': getattr(listing, 'model', ''),
                    'year': getattr(listing, 'year', ''),
                    'petrol': getattr(listing, 'petrol', ''),
                    'car_body': getattr(listing, 'car_body', ''),
                    'mileage': getattr(listing, 'mileage', ''),
                    'color': getattr(listing, 'color', ''),
                    'engine_size': getattr(listing, 'engine_size', ''),
                    'condition': getattr(listing, 'condition', ''),
                    'transmission': getattr(listing, 'transmission', ''),
                    'country_origin': getattr(listing, 'country_origin', ''),
                    'engine_power': getattr(listing, 'engine_power', ''),
                    'drive': getattr(listing, 'drive', ''),
                }
                writer.writerow(row)
