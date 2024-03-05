import json

import requests


#    Creating a variable for the user to input a postcode
userPostcode = input("Enter postcode:")

#    Creating a variable and assigning to our URL and User Agent
JustEatAPI = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{userPostcode}"
userAgent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

#   Creating a variable for our get request
response = requests.get(JustEatAPI, headers=userAgent)

#   Creating a variable for our response
response_content = response.json()


#   Try and except used to handle issues with restaurant data (eg - invalid URL)
try:
    #   Creating a variable for the 'restaurants' property in our json
    restaurant_data = response_content["restaurants"]

    #   If statement to ensure there is still an output when there are less than 10 in the 'restaurants' property
    size = 0
    if len(restaurant_data) >= 10:
        size = 10
    else:
        size = len(restaurant_data)

    #   For loop to print the first 10 restaurants along with the 4 data points: name, cuisine, rating and address
    for i in range(0, size):
        print("Restaurant", i+1, ":")
        print(" Name:", restaurant_data[i]['name'])
        print(" Cuisine:", restaurant_data[i]['cuisines'][0]['name'])
        print(" Star Rating:", restaurant_data[i]['rating']['starRating'])
        print(" Full Address:", restaurant_data[i]['address'])
        print("--------------------")

except:
    print("Unable to retrieve restaurant information.")

#   'Finally' message displays regardless of what happens in the try and except
finally:
    print("Number of restaurants found within postcode:", size)
    print("Postcode --> Restaurant scan complete.")



