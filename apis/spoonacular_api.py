import requests
import json

_API_KEY = "39c6f0544b8a4abebfe859c409c2ce35"
_BASE_PATH = "https://api.spoonacular.com/"

def get_random_recipes(num_recipes: int = 1):

    params = {
        "number": num_recipes,
        "apiKey": _API_KEY,
    }

    response = requests.get(_BASE_PATH + "recipes/random", params=params)

    if response.status_code == 200:
        json_response = response.json()
        recipes = json_response["recipes"]
        recipe = recipes[0]
        #print(json_response)
        #print(type(json_response))
        for k, v in recipe.items():
            print(k)
        #ingredients = json_response["extendedIngredients"]
        #print(ingredients)
    else:
        print(f"Failed to retrieve recipe. Status code: {response.status_code}")

get_random_recipes()