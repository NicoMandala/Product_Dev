from fastapi import FastAPI
import requests

# Initially I assumed that the ingredient names would be enough but the task B,I realized we need measurements as well. Note: Not all drinks have measurements and the units vary too. 
# Initially I retrieved the API response as is which led to unclean response. Once it's switched to JSON, it's easier to parse the response.

app = FastAPI()

@app.get("/random_cocktail")
def get_random_cocktail():
    # Make a request to the cocktail API to get a random cocktail
    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/random.php")
    data = response.json()

    # Extract the cocktail details from the response
    cocktail = data["drinks"][0]
    name = cocktail["strDrink"]
    tagline = cocktail["strTags"]
    ingredients = []
    instructions = cocktail["strInstructions"]

    # Extract the ingredients and their measurements
    for i in range(1, 16):
        ingredient = cocktail[f"strIngredient{i}"]
        measurement = cocktail[f"strMeasure{i}"]
        if ingredient:
            ingredients.append(f"{ingredient} - {measurement}")

    # Return the cocktail details
    return {
        "name": name,
        "tagline": tagline,
        "ingredients": ingredients,
        "instructions": instructions
    }