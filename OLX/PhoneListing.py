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
