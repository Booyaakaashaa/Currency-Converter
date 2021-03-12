import json
import requests


def main():
    cache = {}
    currency_code = input().lower()
    url = f"http://www.floatrates.com/daily/{currency_code}.json"
    data = requests.get(url)
    json_data = json.loads(data.text)
    if currency_code == 'usd':
        cache['usd'] = {'rate': 1}
    else:
        cache["usd"] = json_data["usd"]
    if currency_code == 'eur':
        cache['eur'] = {'rate': 1}
    else:
        cache["eur"] = json_data["eur"]
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
            cache[out_currency] = json_data[out_currency]
            print(f"You received {amount * cache[out_currency]['rate']} {out_currency}.")


if __name__ == "__main__":
    main()
