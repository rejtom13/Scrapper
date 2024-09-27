import json
import re

import requests


class OlxList:
    @staticmethod
    def get_olx_listings(url, page):
        if '?' in url:
            url = f'{url}&page={page}'
        else:
            url = f'{url}?page={page}'
        response = requests.get(url)
        match = re.search('__PRERENDERED_STATE__\s*=\s*\"({.*?})\";', response.text)
        cleaned_content = match.group(1)

        # Fix any escaped slashes or unicode escapes
        cleaned_content = cleaned_content.replace('\\"', '"')  # Handle escaped double quotes
        cleaned_content = cleaned_content.replace('\\\\', '\\')  # Handle double backslashes
        data = json.loads(cleaned_content)
        return data['listing']['listing']['ads']

