import json

import requests

URL = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/W116RN"
userAgent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

response = requests.get(URL, headers=userAgent)

try:

    if str(response.status_code).startswith("2"):
        print(json.dumps(response.json(), indent=2))
    elif str(response.status_code).startswith("4"):
        print("Client side error:", response.status_code)
    elif str(response.status_code).startswith("5"):
        print("Server side error:", response.status_code)
    else:
        print("Failed with status code:", response.status_code)

except Exception as x:
    print("Unexpected error occurred:", x)




