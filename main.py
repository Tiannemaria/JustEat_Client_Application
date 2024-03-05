import json

import requests

URL = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC1V1NR"
userAgent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

response = requests.get(URL, headers=userAgent)

response_content = response.json()
# try:
#
#     if str(response.status_code).startswith("2"):
#         print(json.dumps(response.json(), indent=2))
#     elif str(response.status_code).startswith("4"):
#         print("Client side error:", response.status_code)
#     elif str(response.status_code).startswith("5"):
#         print("Server side error:", response.status_code)
#     else:
#         print("Failed with status code:", response.status_code)
#
# except Exception as x:
#     print("Unexpected error occurred:", x)


with open("response.json", "w") as file:
    json.dump(response_content, file, indent=4)

print("Response written to 'response.json' file.")

restaurant_data = response_content["restaurants"]

with open("restaurants.json", "w") as file:
    json.dump(restaurant_data, file, indent=4)

for i in range(0, 10):
    print("restaurant {}:".format(i+1))
    print("     name:", restaurant_data[i]['name'])
    print("     Star rating:", restaurant_data[i]['rating']['starRating'])
    print("     Postal Code:", restaurant_data[i]['address']['postalCode'])
    print("     Cuisine:", restaurant_data[i]['cuisines'][0]['name'])
