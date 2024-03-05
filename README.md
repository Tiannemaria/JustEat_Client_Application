# JustEat_Client_Application

OVERVIEW:
This script is designed to provide data from restaurants using the JustEat API - specifically extracting the first 10 restaurants along with 4 data points, the restaurant's: name, cuisine, rating (as a number) and address.

Imports used in this script: 
import json
import requests

Breakdown of the code:
- User input: Prompts the user to input a postcode, which is added onto the API's URL.
- Creating the API request: variables are implemented for the API's URL, user agent, get request and json response.
- The json response: the script extracts data from the "restaurants" property of the json response and is assigned to a variable.
- Printing the restaurant information: the script prints data from the first 10 restaurants along with their name, cuisine, rating and address by using a for loop.
- Try and except: try and except is implemented to handle issues with restaurant data.
- Finally: finally block ensures a message is printed regardless of the output.


Assumptions or things that weren't clear:
- It wasn't clear what the output should be if a postcode provided less than 10 restaurants. To remedy this, I implemented an if statement to ensure that there is still an output even if the user provides a postcode with under 10 restaurants nearby.

- When outputting the address of the first 10 restaurants, it wasn't clear what elements of the address to include. For example, should the 'address' just include the city and postcode? Or include the location type and coordinates too? To remedy this, I included all data points related to the address of the restaurants so that all elements were covered.

Improvements I'd make to my solution:
- To improve my solution, I would ask the user if they want to search another postcode to find 10 restaurants within that area. To do this, I would implement a while loop to enable my code to loop whilst the user still wants to enter a postcode. 
