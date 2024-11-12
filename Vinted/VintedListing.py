from typing import Any, Dict

from bs4 import BeautifulSoup


class VintedListing:
    """Reprezentuje ogłoszenie z jego szczegółami."""

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Inicjalizuje obiekt Listing.

        Args:
            data (Dict[str, Any]): Słownik zawierający informacje o ogłoszeniu.
        """
        self.title: str = data.get('title', '') if data.get('title') else ''
        self.id: str = data.get('id', '') if data.get('id') else ''
        self.url: str = data.get('url', '') if data.get('url') else ''
        self.image_url: str = data.get('photo', '').get('url','') if data.get('url') else ''
        self.price: float = float(data.get('total_item_price',  0.0).get('amount',0.0) if data.get('amount') else 0.0)
        self.state: str = data.get('status', '') if data.get('status') else ''
        self.description: str = ''



    def __repr__(self) -> str:
        return f"Listing( title={self.title}, price={self.price}, date={self.created_date})"
