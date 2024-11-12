import requests
import json


class DiscordWebhookSender:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_phone_listing(self, listing):
        embed = {
            "title": listing.title,
            "url": listing.url,
            "description": listing.description,
            "thumbnail": {"url": listing.image_url},
            "fields": [
                {"name": "Strona", "value": f"{listing.page}", "inline": True},
                {"name": "Wysyłka", "value": f"{listing.isDelivery}", "inline": True},
                {"name": "Stan", "value": f"{listing.state}", "inline": True},
                {"name": "Pamieć", "value": f"{listing.builtinmemory_phones}", "inline": True},
                {"name": "Model", "value": f"{listing.phonemodel}", "inline": True},
                {"name": "Cena", "value": f"{listing.price} zł", "inline": True},
                {"name": "User", "value": f"{listing.user}", "inline": False},
                {"name": "", "value": f"{listing.rate}", "inline": False},

            ]
        }

        data = {
            "embeds": [embed]
        }
        response = requests.post(self.webhook_url, json=data)
        if response.status_code == 204:
            print(f"Nowe ogłoszenie:Price: {listing.price} {listing.title}")
        else:
            print(f"Błąd podczas wysyłania wiadomości: {response.status_code} - {response.text}")



