from typing import Any, Dict

from bs4 import BeautifulSoup


class Listing:
    """Reprezentuje ogłoszenie z jego szczegółami."""

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Inicjalizuje obiekt Listing.

        Args:
            data (Dict[str, Any]): Słownik zawierający informacje o ogłoszeniu.
        """
        self.title: str = data.get('title', '') if data.get('title') else ''
        self.id: str = data.get('id', '') if data.get('id') else ''
        self.page: str = 'OLX'
        self.image_url: str = data.get('photos', [''])[0] if data.get('photos') and isinstance(data.get('photos'),
                                                                                               list) else ''
        self.location: str = data.get('location', {}).get('pathName', '') if data.get('location') else ''
        self.url: str = data.get('url', '') if data.get('url') else ''

        price_data = data.get('price', {})
        if price_data and isinstance(price_data, dict):
            regular_price = price_data.get('regularPrice', {})
            self.price = regular_price.get('value', 0.0) if isinstance(regular_price, dict) else 0.0
        else:
            self.price = 0.0

        self.description: str =BeautifulSoup(data.get('description', '') if data.get('description') else '', "html.parser").get_text()

        delivery_data = data.get('delivery', {})
        if delivery_data and isinstance(delivery_data, dict):
            self.isDelivery = delivery_data.get('rock', '').get('mode', '')
        else:
            self.isDelivery = ''

        self.created_date: str = data.get('createdTime', '') if data.get('createdTime') else ''

    def __repr__(self) -> str:
        return f"Listing(title={self.title}, price={self.price}, date={self.created_date})"
