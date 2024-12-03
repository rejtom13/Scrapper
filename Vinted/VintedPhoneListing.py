import json
import time
from traceback import print_tb
from typing import Any, Dict

import requests

from OLX.Listing import Listing
from Vinted.VintedListing import VintedListing

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
        self.user: str = ''
        self.username: str = ''
        self.photo_list = []
        self.rate = ''
        self.recommendation = self.get_recommendation(self.phonemodel)
        self.blacklist = ['oskareqq0', 'adrianna785', 'stefanmaniak', 'ninakolodziej03', 'viintedsprzedazjacek',
                          'jarusz97', 'wiktorrcloud', 'kacperhl', 'karolinka992210', 'spejsonpucha']
        self.isDeal: bool = self.check_is_deal()


    def get_model_name_by_id(self, model_id):
        model_data = {
            "models": [
                {
                    "id": 4020,
                    "name": "iphone-1",
                    "metadata": {
                        "collection_id": 4020
                    },
                    "children": []
                },
                {
                    "id": 4041,
                    "name": "iphone-11",
                    "metadata": {
                        "collection_id": 4041
                    },
                    "children": []
                },
                {
                    "id": 4042,
                    "name": "iphone-11 Pro",
                    "metadata": {
                        "collection_id": 4042
                    },
                    "children": []
                },
                {
                    "id": 4043,
                    "name": "iphone-11 Pro Max",
                    "metadata": {
                        "collection_id": 4043
                    },
                    "children": []
                },
                {
                    "id": 4044,
                    "name": "iphone-12",
                    "metadata": {
                        "collection_id": 4044
                    },
                    "children": []
                },
                {
                    "id": 4045,
                    "name": "iphone-12 mini",
                    "metadata": {
                        "collection_id": 4045
                    },
                    "children": []
                },
                {
                    "id": 4046,
                    "name": "iphone-12 Pro",
                    "metadata": {
                        "collection_id": 4046
                    },
                    "children": []
                },
                {
                    "id": 4047,
                    "name": "iphone-12 Pro Max",
                    "metadata": {
                        "collection_id": 4047
                    },
                    "children": []
                },
                {
                    "id": 4048,
                    "name": "iphone-13",
                    "metadata": {
                        "collection_id": 4048
                    },
                    "children": []
                },
                {
                    "id": 4049,
                    "name": "iphone-13 mini",
                    "metadata": {
                        "collection_id": 4049
                    },
                    "children": []
                },
                {
                    "id": 4050,
                    "name": "iphone-13 Pro",
                    "metadata": {
                        "collection_id": 4050
                    },
                    "children": []
                },
                {
                    "id": 4051,
                    "name": "iphone-13 Pro Max",
                    "metadata": {
                        "collection_id": 4051
                    },
                    "children": []
                },
                {
                    "id": 4052,
                    "name": "iphone-14",
                    "metadata": {
                        "collection_id": 4052
                    },
                    "children": []
                },
                {
                    "id": 4053,
                    "name": "iphone-14 Plus",
                    "metadata": {
                        "collection_id": 4053
                    },
                    "children": []
                },
                {
                    "id": 4054,
                    "name": "iphone-14 Pro",
                    "metadata": {
                        "collection_id": 4054
                    },
                    "children": []
                },
                {
                    "id": 4055,
                    "name": "iphone-14 Pro Max",
                    "metadata": {
                        "collection_id": 4055
                    },
                    "children": []
                },
                {
                    "id": 4056,
                    "name": "iphone-15",
                    "metadata": {
                        "collection_id": 4056
                    },
                    "children": []
                },
                {
                    "id": 4057,
                    "name": "iphone-15 Plus",
                    "metadata": {
                        "collection_id": 4057
                    },
                    "children": []
                },
                {
                    "id": 4058,
                    "name": "iphone-15 Pro",
                    "metadata": {
                        "collection_id": 4058
                    },
                    "children": []
                },
                {
                    "id": 4059,
                    "name": "iphone-15 Pro Max",
                    "metadata": {
                        "collection_id": 4059
                    },
                    "children": []
                },
                {
                    "id": 4021,
                    "name": "iphone-3G",
                    "metadata": {
                        "collection_id": 4021
                    },
                    "children": []
                },
                {
                    "id": 4022,
                    "name": "iphone-3GS",
                    "metadata": {
                        "collection_id": 4022
                    },
                    "children": []
                },
                {
                    "id": 4023,
                    "name": "iphone-4",
                    "metadata": {
                        "collection_id": 4023
                    },
                    "children": []
                },
                {
                    "id": 4024,
                    "name": "iphone-4s",
                    "metadata": {
                        "collection_id": 4024
                    },
                    "children": []
                },
                {
                    "id": 4025,
                    "name": "iphone-5",
                    "metadata": {
                        "collection_id": 4025
                    },
                    "children": []
                },
                {
                    "id": 4026,
                    "name": "iphone-5C",
                    "metadata": {
                        "collection_id": 4026
                    },
                    "children": []
                },
                {
                    "id": 4027,
                    "name": "iphone-5s",
                    "metadata": {
                        "collection_id": 4027
                    },
                    "children": []
                },
                {
                    "id": 4028,
                    "name": "iphone-6S",
                    "metadata": {
                        "collection_id": 4028
                    },
                    "children": []
                },
                {
                    "id": 4029,
                    "name": "iphone-6S Plus",
                    "metadata": {
                        "collection_id": 4029
                    },
                    "children": []
                },
                {
                    "id": 4030,
                    "name": "iphone-7",
                    "metadata": {
                        "collection_id": 4030
                    },
                    "children": []
                },
                {
                    "id": 4031,
                    "name": "iphone-7 Plus",
                    "metadata": {
                        "collection_id": 4031
                    },
                    "children": []
                },
                {
                    "id": 4032,
                    "name": "iphone-8",
                    "metadata": {
                        "collection_id": 4032
                    },
                    "children": []
                },
                {
                    "id": 4033,
                    "name": "iphone-8 Plus",
                    "metadata": {
                        "collection_id": 4033
                    },
                    "children": []
                },
                {
                    "id": 4034,
                    "name": "iphone-SE (2016)",
                    "metadata": {
                        "collection_id": 4034
                    },
                    "children": []
                },
                {
                    "id": 4035,
                    "name": "iphone-SE (2020)",
                    "metadata": {
                        "collection_id": 4035
                    },
                    "children": []
                },
                {
                    "id": 4036,
                    "name": "iphone-SE (2022)",
                    "metadata": {
                        "collection_id": 4036
                    },
                    "children": []
                },
                {
                    "id": 4037,
                    "name": "iphone-X",
                    "metadata": {
                        "collection_id": 4037
                    },
                    "children": []
                },
                {
                    "id": 4038,
                    "name": "iphone-XR",
                    "metadata": {
                        "collection_id": 4038
                    },
                    "children": []
                },
                {
                    "id": 4039,
                    "name": "iphone-XS",
                    "metadata": {
                        "collection_id": 4039
                    },
                    "children": []
                },
                {
                    "id": 4040,
                    "name": "iphone-XS Max",
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
        return model_id

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
            if int(response.status_code) == 200:
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
                self.username = data['user']['login']
                self.user = f"{data['user']['login']} Items: {data['user']['given_item_count']}/{data['user']['taken_item_count']} Feedback: {data['user']['positive_feedback_count']}/{data['user']['neutral_feedback_count']}/{data['user']['negative_feedback_count']}"
                photos = data.get("photos", [])
                self.photo_list= [photo.get("url") for photo in photos if "url" in photo]
                self.isDeal: bool = self.check_is_deal()
                self.recommendation = self.get_recommendation(self.phonemodel)
                return(data)
            else:
                print(response.status_code)
                print(response.content)

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
            title, imageUrl, location, url, price, description, isDelivery, memory, brand, phonemodel, state, color, listingId, createDate, endDate, page
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s)
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
            self.brand,
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
        if self.price > 0 and self.username not in self.blacklist:
            if  self.phonemodel == 'iphone-11' and self.price <= 450\
            or  self.phonemodel == 'iphone-11 Pro' and self.price <= 500\
            or  self.phonemodel == 'iphone-11 Pro Max' and self.price <= 700\
            or  self.phonemodel == 'iphone-12' and self.price <= 600\
            or  self.phonemodel == 'iphone-12 mini' and self.price <= 650\
            or  self.phonemodel == 'iphone-12 Pro' and self.price <= 900\
            or  self.phonemodel == 'iphone-12 Pro Max' and self.price <= 1100\
            or  self.phonemodel == 'iphone-13' and self.price <= 1050\
            or  self.phonemodel == 'iphone-13 Pro' and self.price <= 1500\
            or  self.phonemodel == 'iphone-13 mini' and self.price <= 800\
            or  self.phonemodel == 'iphone-14' and self.price <= 1400\
            or  self.phonemodel == 'iphone-14 Pro' and self.price <= 2200\
            or  self.phonemodel == 'iphone-14 Pro Max' and self.price <= 2400\
            or  self.phonemodel == 'iphone-14 Plus' and self.price <= 1700\
            or  self.phonemodel == 'iphone-15' and self.price <= 2100\
            or  self.phonemodel == 'iphone-15 Pro' and self.price <= 2850\
            or  self.phonemodel == 'iphone-15 Pro Max' and self.price <= 3300\
            or  self.phonemodel == 'iphone-15 Plus' and self.price <= 2400:
                return True
            else:
                return False

    def get_recommendation(self, model):
        model1= str(model).strip()
        list = {
                'iphone-11': 'Max: 450',
                'iphone-11 Pro': 'Max: 500',
                'iphone-11 Pro Max': 'Max: 700 ',
                'iphone-12': 'Max: 600',
                'iphone-12 mini': 'Max: 650',
                'iphone-12 Pro': 'Max: 900',
                'iphone-12 Pro Max': 'Max: 1100',
                'iphone-13': 'Max: 1000',
                'iphone-13 Pro': 'Max: 1200',
                'iphone-13 mini': 'Max: 800',
                'iphone-14': 'Max: 1400',
                'iphone-14 Pro': 'Max: 2200',
                'iphone-14 Pro Max': 'Max: 2400',
                'iphone-14 Plus': 'Max: 1700',
                'iphone-15': 'Max: 2100',
                'iphone-15 Pro': 'Max: 2850',
                'iphone-15 Pro Max': 'Max: 3300',
                'iphone-15 Plus': 'Max: 2400'
        }
        try:
            return list[model1]
        except:
            return model1

