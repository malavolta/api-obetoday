import requests
import json

def BTC_IN_VES():
    url = "https://localbitcoins.com/api/equation/(bitstampusd_avg*USD_in_VES)/bitstampusd_avg"
    response = requests.get(url)
    return json.loads(response.text)["data"]


def YADIO_RATE_USD():
    url = "https://api.yadio.io/rate/usd"
    response = requests.get(url)
    return json.loads(response.text)["rate"]


def DOLARTODAY_RATE():
    url = "https://s3.amazonaws.com/dolartoday/data.json"
    response = requests.get(url)
    return json.loads(response.text)["USD"]
