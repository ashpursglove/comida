


import requests
import json


api_key = "5387c55dd249460a8a55aa48ebd3ea89"


response = requests.get("https://api.spoonacular.com/food/jokes/random?apiKey=%s" % (api_key))


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# To use the API you need an API key. You can get a free one by simply signing up here.

# Once you have your API key, you have to put it in the request URL for every request you make like so ?apiKey=YOUR-API-KEY.

# Attention: Only the first query parameter is prefixed with a ? (question mark), all subsequent ones will be prefixed with a & (ampersand). That is how URLs work and nothing related to our API. Here's a full example with two parameters apiKey and includeNutrition: 

# https://api.spoonacular.com/recipes/716429/information?apiKey=YOUR-API-KEY&includeNutrition=true.


# Please further note that parameters are case sensitive, it is apiKey not apikey.





#print(response.status_code)
print(response.json())







#jprint(response.json())


