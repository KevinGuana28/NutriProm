import pandas as pd

# Suponiendo que Recipe1M está en formato CSV
recipe1m = pd.read_csv('path_to_recipe1m.csv')

# Crear un mapeo de categorías a ingredientes
category_to_ingredients = {}

for index, row in recipe1m.iterrows():
    category = row['category']
    ingredients = row['ingredients'].split(',')
    if category not in category_to_ingredients:
        category_to_ingredients[category] = set()
    category_to_ingredients[category].update(ingredients)

# Guardar el mapeo en un archivo
import json

with open('ingredient_service/category_to_ingredients.json', 'w') as f:
    json.dump(category_to_ingredients, f)
