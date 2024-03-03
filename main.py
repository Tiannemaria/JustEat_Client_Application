import requests

URL = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC4M7RF"
userAgent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

response = requests.get(URL, headers=userAgent)

if str(response.status_code).startswith("2"):
    print(response.json())
elif str(response.status_code).startswith("4"):
    print("Client side error:", response.status_code)
elif str(response.status_code).startswith("5"):
    print("Server side error:", response.status_code)
else:
    print("Failed with status code:", response.status_code)



