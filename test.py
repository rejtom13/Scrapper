import requests
url = 'https://www.vinted.pl/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Sprawdza, czy odpowiedź była udana

    # Pobiera ciasteczka i tworzy string
    cookies = response.cookies
    temp = "; ".join([f"{cookie.name}={cookie.value}" for cookie in cookies])
    print(temp)
except:
    print('xd')
