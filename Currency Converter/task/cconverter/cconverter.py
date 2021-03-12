import json, requests
currency_code = input().lower()
url = f"http://www.floatrates.com/daily/{currency_code}.json"
data = requests.get(url)
json_data = json.loads(data.text)
print(json_data["usd"], json_data["eur"], sep="\n")
