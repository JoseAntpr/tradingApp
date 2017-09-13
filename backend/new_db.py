import requests
import json
from tradingApp.settings import DEBUG

if DEBUG:
    url = "http://localhost:8000/api/1.0/coins/"
else:
    url = "http://192.168.33.10/api/1.0/coins/"


coins = [
    {"name": "AUD"},
    {"name": "BGN"},
    {"name": "BRL"},
    {"name": "CAD"},
    {"name": "CHF"},
    {"name": "CNY"},
    {"name": "CZK"},
    {"name": "DKK"},
    {"name": "GBP"},
    {"name": "HKD"},
    {"name": "HRK"},
    {"name": "HUF"},
    {"name": "USD"},
    {"name": "RON"},
    {"name": "EUR"},

]

for i in coins:
    print(i)
    r = requests.post(url, json=i)
    print(r.status_code)


