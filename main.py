import json

import requests

response = requests.get("https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC4M7RF")

if response.status_code == 200:

    print(response.json())
else:

    print(f"Error: {response.status_code}")

