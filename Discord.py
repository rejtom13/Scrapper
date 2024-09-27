import requests
import json


class DiscordWebhookSender:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_listing(self, listing):
        # Tworzymy strukturę embedu w formacie JSON
        embed = {
            "title": listing.title,
            "url": listing.url,
            "description": listing.description,
            "thumbnail": {"url": listing.image_url},
            "fields": [
                {"name": "Cena", "value": f"{listing.price} zł", "inline": False},
            ]
        }

        data = {
            "embeds": [embed]
        }

        # Wysyłanie POST requesta do webhooka
        response = requests.post(self.webhook_url, json=data)

        # Sprawdzamy, czy wysłanie powiodło się
        if response.status_code == 204:
            print("Wiadomość wysłana pomyślnie.")
        else:
            print(f"Błąd podczas wysyłania wiadomości: {response.status_code} - {response.text}")




