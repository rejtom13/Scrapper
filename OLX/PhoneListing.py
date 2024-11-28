from typing import Any, Dict
from OLX.Listing import Listing


class PhoneListing(Listing):
    """Reprezentuje ogłoszenie telefonu z dodatkowymi szczegółami."""

    def __init__(self, data: Dict[str, Any]) -> None:
        super().__init__(data)
        params = data.get('params', [])
        params_dict = {param['key']: param.get('normalizedValue', param.get('value', '')) for param in params}

        self.builtinmemory_phones: str = params_dict.get('builtinmemory_phones', '')
        self.color: str = params_dict.get('coloriphone', '')
        self.state: str = params_dict.get('state', '')
        self.phonemodel: str = params_dict.get('phonemodel', '')
        self.page: str = 'OLX'  # Dodanie pola 'page', jeśli jest obecne w danych
        self.listing_id: str = data.get('id', '')  # Dodanie pola 'listingId', jeśli jest obecne w danych
        self.isDeal: bool = self.check_is_deal()
        self.recommendation = self.get_recommendation(self.phonemodel)
        self.rate: str = ''



    def save_to_db(self, db_connection) -> None:
        """
        Zapisuje ogłoszenie do bazy danych.

        Args:
            db_connection: Obiekt połączenia do bazy danych (np. DbConnection).
        """
        cursor = db_connection.cnx.cursor()  # Użycie kursora z obiektu połączenia

        # Tworzymy zapytanie SQL do wstawienia danych do tabeli
        sql = """
        INSERT INTO listings (
            title, imageUrl, location, url, price, description, isDelivery, memory, phonemodel, state, color, listingId, createDate, endDate, page
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Przekazujemy dane do zapytania
        values = (
            self.title,
            self.image_url,
            self.location,
            self.url,
            self.price,
            self.description,
            self.isDelivery,
            self.builtinmemory_phones,
            self.phonemodel,
            self.state,
            self.color,
            self.listing_id,  # Wcześniej było przypisanie self.color, co było błędne
            self.created_date,
            None,  # Domyślnie wartość endDate jako None
            self.page  # Dodanie pola 'page' do wartości
        )

        # Wykonanie zapytania i zapisanie danych w bazie
        cursor.execute(sql, values)
        db_connection.cnx.commit()

        # Zamknięcie kursora po zakończeniu operacji
        cursor.close()

    def check_is_deal(self):
        price_limits = {
            'iphone-11': 400,
            'iphone-11-pro': 500,
            'iphone-11-pro-max': 700,
            'iphone-12': 600,
            'iphone-12-mini': 550,
            'iphone-12-pro': 900,
            'iphone-12-pro-max': 900,
            'iphone-13': 1000,
            'iphone-13-pro': 1500,
            'iphone-13-mini': 800,
            'iphone-14': 1400,
            'iphone-14-pro': 2200,
            'iphone-14-pro-max': 2400,
            'iphone-14-plus': 1700,
            'iphone-15': 2100,
            'iphone-15-pro': 2850,
            'iphone-15-pro-max': 3300,
            'iphone-15-plus': 2400,
            # Dodaj więcej modeli, jeśli to konieczne
        }

        # Sprawdź, czy model istnieje w słowniku i czy Max jest w limicie
        if self.price > 0 and self.phonemodel in price_limits:
            return self.price <= price_limits[self.phonemodel]
        return False

    def get_recommendation(self, model):
        list = {
            'iphone-11': 'Max: 450',
            'iphone-11-pro': 'Max: 500',
            'iphone-11-pro-max': 'Max: 700 ',
            'iphone-12': 'Max: 600',
            'iphone-12-mini': 'Max: 550',
            'iphone-12-pro': 'Max: 900',
            'iphone-12-pro-max': 'Max: 1100',
            'iphone-13': 'Max: 1000',
            'iphone-13-pro': 'Max: 1200',
            'iphone-13-mini': 'Max: 800',
            'iphone-14': 'Max: 1400',
            'iphone-14-pro': 'Max: 2200',
            'iphone-14-pro-max': 'Max: 2400',
            'iphone-14-plus': 'Max: 1700',
            'iphone-15': 'Max: 2100',
            'iphone-15-pro': 'Max: 2850',
            'iphone-15-pro-max': 'Max: 3300',
            'iphone-15-plus': 'Max: 2400'
        }
        try:
            return list[model]
        except:
            return ""