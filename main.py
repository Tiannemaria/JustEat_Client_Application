import requests

URL = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC4M7RF"
userAgent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

response = requests.get(URL, headers=userAgent)
response_json = response.json()

print(response_json)

# print(response)
# if response.status_code == 200:
#
#     print(response.json())
# else:
#
#     print(f"Error: {response.status_code}")

