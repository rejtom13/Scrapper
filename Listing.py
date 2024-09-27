from typing import Any, Dict, List, Optional


class Listing:
    """Reprezentuje ogłoszenie z jego szczegółami."""

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Inicjalizuje obiekt Listing.

        Args:
            data (Dict[str, Any]): Słownik zawierający informacje o ogłoszeniu.
        """
        self.title: str = data.get('title', '')
        self.image_url: str = data.get('photos', [''])[0] if data.get('photos') else ''
        self.location: str = data.get('location', {}).get('pathName', '')
        self.url: str = data.get('url', '')
        self.price: float = data.get('price', {}).get('regularPrice', {}).get('value', 0.0)
        self.description: str = data.get('description', '')

    def __repr__(self) -> str:
        return f"Listing(title={self.title}, price={self.price})"
