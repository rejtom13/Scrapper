import json
import re

import requests


class OlxList:
    @staticmethod
    def get_olx_listings_for_monitor(url):
        response = requests.get(url)
        match = re.search('__PRERENDERED_STATE__\s*=\s*\"({.*?})\";', response.text)
        cleaned_content = match.group(1)

        # Fix any escaped slashes or unicode escapes
        cleaned_content = cleaned_content.replace('\\"', '"')  # Handle escaped double quotes
        cleaned_content = cleaned_content.replace('\\\\', '\\')  # Handle double backslashes
        data = json.loads(cleaned_content)
        try:
            return data['listing']['listing']['ads']
        except:
            print(data)

    @staticmethod
    def get_olx_listings(url, page=1):
        # if '?' in url:
        #     print(url)
        #     olx_url = f'{url}&page={page}'
        # else:
        #     olx_url = f'{url}?page={page}'
        olx_url = f'{url}&page={page}'
        print(f'{url}&page={page}')
        response = requests.get(olx_url)
        match = re.search('__PRERENDERED_STATE__\s*=\s*\"({.*?})\";', response.text)
        cleaned_content = match.group(1)

        # Fix any escaped slashes or unicode escapes
        cleaned_content = cleaned_content.replace('\\"', '"')  # Handle escaped double quotes
        cleaned_content = cleaned_content.replace('\\\\', '\\')  # Handle double backslashes
        data = json.loads(cleaned_content)
        try:
            return data['listing']['listing']['ads'], data['listing']['listing']['totalPages']
        except:
            print(data)

