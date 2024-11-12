import json
import random
import requests

class Proxy:
    def __init__(self):
        self.proxy_list = self.get_proxy_list()

    def get_proxy_list(self):
        response = requests.get(
            "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=100",
            headers={"Authorization": "ijrpwokntyg9c4ags6h9zozccksvz7nx4egm877z"}
        )

        data = json.loads(response.content)
        proxy_list = []

        for proxy in data['results']:
            proxy_entry = {
                'http': f"http://{proxy['username']}:{proxy['password']}@{proxy['proxy_address']}:{proxy['port']}",
                'https': f"http://{proxy['username']}:{proxy['password']}@{proxy['proxy_address']}:{proxy['port']}"
            }
            proxy_list.append(proxy_entry)

        return proxy_list
