import json
import random
import time
import requests

from Proxy import Proxy

class VintedList:
    def __init__(self, proxy_list):
        self.proxy_list = proxy_list
        self.proxy = self.set_proxy()
        self.cookies = self.fetch_cookies('https://www.vinted.pl/')

    def set_proxy(self):
        return random.choice(self.proxy_list)

    def fetch_cookies(self, url, max_retries=5):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
        }
        for attempt in range(max_retries):
            try:
                response = requests.get(url, headers=headers, proxies=self.proxy)
                response.raise_for_status()
                cookies = response.cookies
                temp = "; ".join([f"{cookie.name}={cookie.value}" for cookie in cookies])
                return temp
            except requests.RequestException as e:
                print(f"Błąd podczas pobierania ciasteczek (próba {attempt + 1}): {e}")
                time.sleep(1)  # Opcjonalnie poczekaj przed ponowną próbą
                self.proxy = self.set_proxy()
        print("Nie udało się pobrać ciasteczek po maksymalnej liczbie prób.")
        return None

    def get_vinted_list(self, list_url, max_retries=5):
        if not self.cookies:
            print("Brak ciasteczek. Nie można kontynuować.")
            return []

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'cookie': self.cookies,
            'pragma': 'no-cache',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
        }

        for attempt in range(max_retries):
            try:
                response = requests.get(list_url, headers=headers, proxies=self.proxy)
                response.raise_for_status()
                data = json.loads(response.content)
                return data.get('items', [])
            except (requests.RequestException, json.JSONDecodeError) as e:
                print(f"Nie udało się pobrać listingów (próba {attempt + 1}): {e}")
                time.sleep(1)  # Opcjonalnie poczekaj przed ponowną próbą
                self.cookies = self.fetch_cookies('https://www.vinted.pl/')
                headers['cookie'] = self.cookies
        print("Nie udało się pobrać listingów po maksymalnej liczbie prób.")
        return []
