import time
from mysql.connector import connection, errorcode, Error

class DbConnection:
    def __init__(self):
        self.username = "admin"
        self.password = "Test123!"
        self.host = "amazondb2.c38qioco22al.eu-north-1.rds.amazonaws.com"
        self.db_name = "amazondb2"
        self.connect()

    def connect(self):
        try:
            self.cnx = connection.MySQLConnection(user=self.username, password=self.password,
                                                  host=self.host,
                                                  database=self.db_name)
            self.cursor = self.cnx.cursor(buffered=True)  # Utwórz kursora
            self.record_counter = 0
        except Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            self.retry_connection()

    def retry_connection(self):
        print("Retrying connection...")
        time.sleep(5)
        self.connect()

    def close_connection(self):
        self.cursor.close()
        self.cnx.close()

    def increase_counter(self):
        self.record_counter += 1

    def commit_transaction_if_more_than_100(self):
        if self.record_counter > 100:
            try:
                self.cnx.commit()
                self.record_counter = 0
            except Error as err:
                print(f"Commit failed: {err}")
                self.retry_connection()

    def commit_transaction(self):
        try:
            self.cnx.commit()
            self.record_counter = 0
        except Error as err:
            print(f"Commit failed: {err}")
            self.retry_connection()

    def get_all_listing_ids(db_connection) -> list:
        """
        Pobiera wszystkie listing_id z bazy danych.

        Args:
            db_connection: Obiekt połączenia do bazy danych (np. DbConnection).

        Returns:
            list: Lista wszystkich listing_id z tabeli listings.
        """
        cursor = db_connection.cnx.cursor()

        # Zapytanie SQL, które pobiera wszystkie listing_id
        sql = "SELECT listingId FROM listings"

        # Wykonanie zapytania
        cursor.execute(sql)

        # Pobranie wszystkich wyników
        results = cursor.fetchall()

        # Zamykamy kursor po zakończeniu operacji
        cursor.close()

        # Zwracamy listę `listing_id` (każdy rekord w results to krotka, więc wyciągamy pierwszy element z każdej krotki)
        return [str(row[0]) for row in results]
