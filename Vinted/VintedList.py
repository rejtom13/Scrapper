import json
import random
import time

import requests

from Proxy import Proxy

PROXY_LIST = [

    {
        'http': 'http://wvtghrmv:ew6gx6r703d8@31.56.145.17:6601',
        'https': 'http://wvtghrmv:ew6gx6r703d8@31.56.145.17:6601'
    },
]

class VintedList:
    def __init__(self, proxy_list):
        self.proxy_list = proxy_list
        self.proxy = self.set_proxy()
        self.cookies = self.fetch_cookies('https://www.vinted.pl/')

    def set_proxy(self):
        index = random.randint(0, 99)
        return self.proxy_list[index]

    def fetch_cookies(self,url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
        }
        try:
            response = requests.get(url, headers=headers,proxies=self.proxy)
            response.raise_for_status()  # Sprawdza, czy odpowiedź była udana

            # Pobiera ciasteczka i tworzy string
            cookies = response.cookies
            temp = "; ".join([f"{cookie.name}={cookie.value}" for cookie in cookies])
            return temp
        except requests.RequestException as e:
            self.proxy = self.set_proxy()
            print("Błąd podczas pobierania ciasteczek:", e)
            return None


    def get_vinted_list(self, list_url):

        if self.cookies:
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'no-cache',
                'cookie': self.cookies,
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

            try:
                response = requests.get(list_url, headers=headers,proxies=self.proxy)
                data = json.loads(response.content)
                return(data['items'])
            except:
                self.cookies = self.fetch_cookies('https://www.vinted.pl/')
                print(f'Nie pobrało listingów: {self.proxy}')
                return []

