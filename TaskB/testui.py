import matplotlib.pyplot as plt
import json
import requests
from fractions import Fraction 
# improvements needed
# make a note of all the units and their conversions and implement them in the code
# some fractions like 1/3 are not being parsed correctly 



# Function to get a random cocktail recipe
response = requests.get('http://127.0.0.1:8000/random_cocktail/')

# Function to visualize a cocktail recipe
def visualize_cocktail_recipe(cocktail_json):
    # Parse the cocktail JSON data
    cocktail = json.loads(cocktail_json)
    name = cocktail.get('name', 'Unknown Cocktail')
    tagline = cocktail.get('tagline', '')
    ingredients = cocktail.get('ingredients', [])
    instructions = cocktail.get('instructions', 'No instructions provided.')

    # Create a formatted text for displaying cocktail details
    recipe_info = f"**Name**: {name}\n**Tagline**: {tagline}\n\n**Ingredients**:\n"
    for ingredient in ingredients:
        recipe_info += f"- {ingredient}\n"
    recipe_info += f"\n**Instructions**: {instructions}"

    # Create a visual representation of the cocktail ingredients
    fig, ax = plt.subplots(figsize=(3, 6))
    total_quantity = sum([float(ingredient.split(" - ")[1].split()[0]) for ingredient in ingredients if " - " in ingredient])
    # try:
    #     total_quantity = sum([float(ingredient.split(" - ")[1].split()[0]) for ingredient in ingredients if " - " in ingredient])
    # except:
    #     total_quantity = sum([float(Fraction(ingredient.split(" - ")[1].split()[0])) for ingredient in ingredients if " - " in ingredient])

    y_offset = 0

    for ingredient in reversed(ingredients):
        ingredient_name = ingredient
        parts = ingredient.split(" - ")
        # ingredient_name = parts[0] + "-" parts[1]

        if len(parts) ==2:
            try:
                quantity_value = float(parts[1].split()[0]) 
            except ValueError:
                quantity_value = float(Fraction(parts[1].split()[0]))

        height = (quantity_value / total_quantity) * len(ingredients)
        ax.fill_between([0, 1], y_offset, y_offset + height, label=ingredient_name, alpha=0.7)
        y_offset += height

    ax.set_xlim(0, 1)
    ax.set_ylim(0, len(ingredients))
    ax.axis('off')
    ax.legend(loc='upper right')
    plt.suptitle('Cocktail Ingredients')
    plt.title(instructions)
    plt.show()



# Sample cocktail JSON data
sample_cocktail = json.dumps(response.json())

# Test the function
visualize_cocktail_recipe(sample_cocktail)
