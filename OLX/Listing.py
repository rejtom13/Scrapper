import json
from datetime import datetime
from typing import Any, Dict

import requests
from bs4 import BeautifulSoup


class Listing:
    """Reprezentuje ogłoszenie z jego szczegółami."""

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Inicjalizuje obiekt Listing.

        Args:
            data (Dict[str, Any]): Słownik zawierający informacje o ogłoszeniu.
        """
        self.data = data
        self.title: str = data.get('title', '') if data.get('title') else ''
        self.id: str = data.get('id', '') if data.get('id') else ''
        self.page: str = 'OLX'
        self.image_url: str = data.get('photos', [''])[0] if data.get('photos') and isinstance(data.get('photos'),
                                                                                               list) else ''
        self.location: str = data.get('location', {}).get('pathName', '') if data.get('location') else ''
        self.url: str = data.get('url', '') if data.get('url') else ''
        self.isDelivery: str = 'Yes'

        price_data = data.get('price', {})
        if price_data and isinstance(price_data, dict):
            regular_price = price_data.get('regularPrice', {})
            self.price = regular_price.get('value', 0.0) if isinstance(regular_price, dict) else 0.0
        else:
            self.price = 0.0

        self.description: str =BeautifulSoup(data.get('description', '') if data.get('description') else '', "html.parser").get_text()
        self.user: str = ""

        delivery_data = data.get('delivery', {})
        if delivery_data and isinstance(delivery_data, dict):
            self.isDelivery = delivery_data.get('rock', '').get('mode', '')
        else:
            self.isDelivery = ''

        self.created_date: str = data.get('createdTime', '') if data.get('createdTime') else ''

    def get_other_ads(self, user_id):
        url = f"https://www.olx.pl/api/v1/offers/?offset=0&limit=10&category_id=0&sort_by=created_at%3Adesc&query=&user_id={user_id}&owner_type=&facets=%5B%7B%22field%22%3A%22category%22%2C%22limit%22%3A150%7D%5D&last_seen_id="

        payload = {}
        headers = {
            'accept': '*/*',
            'accept-language': 'pl',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.olx.pl/oferty/uzytkownik/4u7Vv/',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
            'x-platform-type': 'mobile-html5',
            'Cookie': 'PHPSESSID=m577bbn99mjfi2ct6kp4envbgo'
            }

        response = requests.request("GET", url, headers=headers, data=payload)
        seller_data = json.loads(response.content)
        return int(seller_data['metadata']['visible_total_count'])

    def get_user(self, ):
        user_data = self.data.get('user', {})
        try:
            ads_count = self.get_other_ads(user_data['id'])
            if ads_count > 1:
                otherads = ':white_check_mark:'
            else:
                otherads = ':x:'
            self.user = f"Name: **{user_data.get('name', '')}**, Location: **{self.location}** \nAcc created: **{datetime.fromisoformat(user_data.get('created', '')).strftime('%Y-%m')}**, Inne ogłoszenia: **{ads_count}** {otherads}"
        except:
            self.user = ''

    def __repr__(self) -> str:
        return f"Listing(title={self.title}, price={self.price}, date={self.created_date})"
