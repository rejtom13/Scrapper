import json
import time
from typing import Any, Dict

import requests

from Vinted.VintedListing import VintedListing

PROXY_LIST = [

    {
        'http': 'http://wvtghrmv:ew6gx6r703d8@161.123.152.115:6360',
        'https': 'http://wvtghrmv:ew6gx6r703d8@161.123.152.115:6360'
    },
]
class VintedPhoneListing(VintedListing):

    def __init__(self, data: Dict[str, Any], ) -> None:
        super().__init__(data)
        self.isDelivery = 'Yes'
        self.page: str = 'Vinted'
        self.brand: str = data.get('brand_title', '')

        self.listing_id: str = data.get('id', '')
        self.builtinmemory_phones: str = ''
        self.color: str = ''
        self.phonemodel: str = ''
        self.created_date: str = ''
        self.location: str = ''
        self.isDeal: bool = self.check_is_deal()
        self.user: str = ''
        self.rate = ''


    def get_model_name_by_id(self, model_id):
        model_data = {
    "models": [
        {
            "id": 4020,
            "name": "iPhone 1",
            "metadata": {
                "collection_id": 4020
            },
            "children": []
        },
        {
            "id": 4041,
            "name": "iPhone 11",
            "metadata": {
                "collection_id": 4041
            },
            "children": []
        },
        {
            "id": 4042,
            "name": "iPhone 11 Pro",
            "metadata": {
                "collection_id": 4042
            },
            "children": []
        },
        {
            "id": 4043,
            "name": "iPhone 11 Pro Max",
            "metadata": {
                "collection_id": 4043
            },
            "children": []
        },
        {
            "id": 4044,
            "name": "iPhone 12",
            "metadata": {
                "collection_id": 4044
            },
            "children": []
        },
        {
            "id": 4045,
            "name": "iPhone 12 mini",
            "metadata": {
                "collection_id": 4045
            },
            "children": []
        },
        {
            "id": 4046,
            "name": "iPhone 12 Pro",
            "metadata": {
                "collection_id": 4046
            },
            "children": []
        },
        {
            "id": 4047,
            "name": "iPhone 12 Pro Max",
            "metadata": {
                "collection_id": 4047
            },
            "children": []
        },
        {
            "id": 4048,
            "name": "iPhone 13",
            "metadata": {
                "collection_id": 4048
            },
            "children": []
        },
        {
            "id": 4049,
            "name": "iPhone 13 mini",
            "metadata": {
                "collection_id": 4049
            },
            "children": []
        },
        {
            "id": 4050,
            "name": "iPhone 13 Pro",
            "metadata": {
                "collection_id": 4050
            },
            "children": []
        },
        {
            "id": 4051,
            "name": "iPhone 13 Pro Max",
            "metadata": {
                "collection_id": 4051
            },
            "children": []
        },
        {
            "id": 4052,
            "name": "iPhone 14",
            "metadata": {
                "collection_id": 4052
            },
            "children": []
        },
        {
            "id": 4053,
            "name": "iPhone 14 Plus",
            "metadata": {
                "collection_id": 4053
            },
            "children": []
        },
        {
            "id": 4054,
            "name": "iPhone 14 Pro",
            "metadata": {
                "collection_id": 4054
            },
            "children": []
        },
        {
            "id": 4055,
            "name": "iPhone 14 Pro Max",
            "metadata": {
                "collection_id": 4055
            },
            "children": []
        },
        {
            "id": 4056,
            "name": "iPhone 15",
            "metadata": {
                "collection_id": 4056
            },
            "children": []
        },
        {
            "id": 4057,
            "name": "iPhone 15 Plus",
            "metadata": {
                "collection_id": 4057
            },
            "children": []
        },
        {
            "id": 4058,
            "name": "iPhone 15 Pro",
            "metadata": {
                "collection_id": 4058
            },
            "children": []
        },
        {
            "id": 4059,
            "name": "iPhone 15 Pro Max",
            "metadata": {
                "collection_id": 4059
            },
            "children": []
        },
        {
            "id": 4021,
            "name": "iPhone 3G",
            "metadata": {
                "collection_id": 4021
            },
            "children": []
        },
        {
            "id": 4022,
            "name": "iPhone 3GS",
            "metadata": {
                "collection_id": 4022
            },
            "children": []
        },
        {
            "id": 4023,
            "name": "iPhone 4",
            "metadata": {
                "collection_id": 4023
            },
            "children": []
        },
        {
            "id": 4024,
            "name": "iPhone 4s",
            "metadata": {
                "collection_id": 4024
            },
            "children": []
        },
        {
            "id": 4025,
            "name": "iPhone 5",
            "metadata": {
                "collection_id": 4025
            },
            "children": []
        },
        {
            "id": 4026,
            "name": "iPhone 5C",
            "metadata": {
                "collection_id": 4026
            },
            "children": []
        },
        {
            "id": 4027,
            "name": "iPhone 5s",
            "metadata": {
                "collection_id": 4027
            },
            "children": []
        },
        {
            "id": 4028,
            "name": "iPhone 6S",
            "metadata": {
                "collection_id": 4028
            },
            "children": []
        },
        {
            "id": 4029,
            "name": "iPhone 6S Plus",
            "metadata": {
                "collection_id": 4029
            },
            "children": []
        },
        {
            "id": 4030,
            "name": "iPhone 7",
            "metadata": {
                "collection_id": 4030
            },
            "children": []
        },
        {
            "id": 4031,
            "name": "iPhone 7 Plus",
            "metadata": {
                "collection_id": 4031
            },
            "children": []
        },
        {
            "id": 4032,
            "name": "iPhone 8",
            "metadata": {
                "collection_id": 4032
            },
            "children": []
        },
        {
            "id": 4033,
            "name": "iPhone 8 Plus",
            "metadata": {
                "collection_id": 4033
            },
            "children": []
        },
        {
            "id": 4034,
            "name": "iPhone SE (2016)",
            "metadata": {
                "collection_id": 4034
            },
            "children": []
        },
        {
            "id": 4035,
            "name": "iPhone SE (2020)",
            "metadata": {
                "collection_id": 4035
            },
            "children": []
        },
        {
            "id": 4036,
            "name": "iPhone SE (2022)",
            "metadata": {
                "collection_id": 4036
            },
            "children": []
        },
        {
            "id": 4037,
            "name": "iPhone X",
            "metadata": {
                "collection_id": 4037
            },
            "children": []
        },
        {
            "id": 4038,
            "name": "iPhone XR",
            "metadata": {
                "collection_id": 4038
            },
            "children": []
        },
        {
            "id": 4039,
            "name": "iPhone XS",
            "metadata": {
                "collection_id": 4039
            },
            "children": []
        },
        {
            "id": 4040,
            "name": "iPhone XS Max",
            "metadata": {
                "collection_id": 4040
            },
            "children": []
        },
        {
                    "id": 4929,
                    "name": "iPad 10.2 (2019)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4930,
                    "name": "iPad 10.2 (2020)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4931,
                    "name": "iPad 10.2 (2021)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4933,
                    "name": "iPad 10.9 (2022)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 5133,
                    "name": "iPad 2",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4925,
                    "name": "iPad 4",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4926,
                    "name": "iPad 9.7 (2017)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4927,
                    "name": "iPad 9.7 (2018)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4934,
                    "name": "iPad Air (2013)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4935,
                    "name": "iPad Air (2014)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4936,
                    "name": "iPad Air (2019)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4937,
                    "name": "iPad Air (2020)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4938,
                    "name": "iPad Air (2022)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 5134,
                    "name": "iPad Air 11 (2024)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 5135,
                    "name": "iPad Air 13 (2024)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4932,
                    "name": "iPad Pro 10.5 (2017)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4944,
                    "name": "iPad Pro 11 (2018)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4945,
                    "name": "iPad Pro 11 (2020)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4946,
                    "name": "iPad Pro 11 (2021)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4947,
                    "name": "iPad Pro 11 (2022)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 5138,
                    "name": "iPad Pro 11 (2024)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4948,
                    "name": "iPad Pro 12.9 (2015)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4949,
                    "name": "iPad Pro 12.9 (2017)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4950,
                    "name": "iPad Pro 12.9 (2018)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4951,
                    "name": "iPad Pro 12.9 (2020)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4952,
                    "name": "iPad Pro 12.9 (2021)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4953,
                    "name": "iPad Pro 12.9 (2022)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 5137,
                    "name": "iPad Pro 13 (2024)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4928,
                    "name": "iPad Pro 9.7 (2016)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4939,
                    "name": "iPad mini (2013)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4940,
                    "name": "iPad mini (2014)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4941,
                    "name": "iPad mini (2015)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4942,
                    "name": "iPad mini (2019)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 4943,
                    "name": "iPad mini (2021)",
                    "type": "default",
                    "description": ""
                },
                {
                    "id": 5136,
                    "name": "iPad mini (2024)",
                    "type": "default",
                    "description": ""
                }
    ],
    "code": 0
}

        for model in model_data["models"]:
            if model["id"] == model_id:
                return model["name"]
        return "Model not found"

    def get_phone_details(self, cookies, proxy):
        list_url = f"https://www.vinted.pl/api/v2/items/{self.listing_id}"
        if cookies:
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'no-cache',
                'cookie': cookies,
                'pragma': 'no-cache',
                'priority': 'u=0, i',
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0'
            }
            response = requests.get(list_url, headers=headers, proxies=proxy)
            try:
                data = (json.loads(response.content))['item']
            except:
                print(response.status_code)
                print(response.content)

            self.phonemodel = self.get_model_name_by_id(data['collection_id'])
            self.description = data['description']
            self.color = data['color1']
            self.created_date = data.get('created_at_ts', '') if data.get('created_at_ts') else ''
            self.location = data.get('country', '') if data.get('country') else ''

            for attribute in data["description_attributes"]:
                if attribute["code"] == "internal_memory_capacity":
                    self.builtinmemory_phones = attribute["value"]
                    break
            self.isDeal = self.check_is_deal()
            self.user = f"{data['user']['login']} Items: {data['user']['given_item_count']}/{data['user']['taken_item_count']} Feedback: {data['user']['positive_feedback_count']}/{data['user']['neutral_feedback_count']}/{data['user']['negative_feedback_count']}"
            return(data)



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
    #
    def check_is_deal(self):
        if self.price > 0:
            if  self.phonemodel == 'iPhone 11' and self.price <= 400\
            or  self.phonemodel == 'iPhone 11 Pro' and self.price <= 500\
            or  self.phonemodel == 'iPhone 11 Pro Max' and self.price <= 700\
            or  self.phonemodel == 'iPhone 12' and self.price <= 600\
            or  self.phonemodel == 'iPhone 12 mini' and self.price <= 550\
            or  self.phonemodel == 'iPhone 12 Pro' and self.price <= 900\
            or  self.phonemodel == 'iPhone 12 Pro Max' and self.price <= 1100\
            or  self.phonemodel == 'iPhone 13' and self.price <= 1050\
            or  self.phonemodel == 'iPhone 13 Pro' and self.price <= 1500\
            or  self.phonemodel == 'iPhone 13 mini' and self.price <= 800\
            or  self.phonemodel == 'iPhone 14' and self.price <= 1400\
            or  self.phonemodel == 'iPhone 14 Pro' and self.price <= 2200\
            or  self.phonemodel == 'iPhone 14 Pro Max' and self.price <= 2400\
            or  self.phonemodel == 'iPhone 14 Plus' and self.price <= 1700\
            or  self.phonemodel == 'iPhone 15' and self.price <= 2100\
            or  self.phonemodel == 'iPhone 15 Pro' and self.price <= 2850\
            or  self.phonemodel == 'iPhone 15 Pro Max' and self.price <= 3300\
            or  self.phonemodel == 'iPhone 15 Plus' and self.price <= 2400:
                return True
            else:
                return False