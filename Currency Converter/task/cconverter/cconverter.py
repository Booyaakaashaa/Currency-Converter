import json
import requests


def main():
    cache = {}
    currency_code = input().lower()
    while 1:
        out_currency = input().lower()

        if not out_currency:
            break
        amount = float(input())

        print("Checking the cache...")
        try:
            if cache[out_currency]:
                print("Oh! It is in the cache!")
                print(f"You received {amount * cache[out_currency]['rate']} {out_currency}")
        except KeyError:
            print("Sorry, but it is not in the cache!")

        url = f"http://www.floatrates.com/daily/{currency_code}.json"
        data = requests.get(url)
        json_data = json.loads(data.text)
        cache[out_currency] = json_data[out_currency]
        print(f"You received {amount * cache[out_currency]['rate']} {out_currency}.")
