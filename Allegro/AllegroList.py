import json
import re

import requests
import urllib3
PROXY_LIST = [

    {
        'http': 'http://wvtghrmv:ew6gx6r703d8@207.244.217.165:6712',
        'https': 'http://wvtghrmv:ew6gx6r703d8@207.244.217.165:6712'
    },
]

class AllegroList:
    @staticmethod
    def get_alegroLokalnie_listings_for_monitor(url):
        try:
            response = requests.get(url, proxies=PROXY_LIST[0])
            if response.status_code == 200:
                match = re.search(r'<script type="application/ld\+json">\s*({.*?})\s*</script>', response.text,
                                  re.DOTALL)
                cleaned_content = match.group(1)
                data = json.loads(cleaned_content)
                return data['itemListElement']
            else:
                print(f"Inny status code: {response.status_code}")
                print(response.content)
                return []
        except requests.exceptions.RequestException as e:
                print(f"Request error: {e}")
                return []

        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return []

        except Exception as e:
            print(f"Unexpected error: {e}")
            if response:
                print(f"Response status code: {response.status_code}")
            return []
