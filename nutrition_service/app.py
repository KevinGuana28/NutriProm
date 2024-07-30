from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Cargar la base de datos nutricional
nutrition_db = pd.read_csv('nutrition_database.csv')

def get_nutritional_info(ingredients):
    total_nutrition = {
        'proteins': 0,
        'fats': 0,
        'carbohydrates': 0,
        'sugars': 0
    }

    for ingredient in ingredients:
        nutrition = nutrition_db[nutrition_db['ingredient'] == ingredient]
        if not nutrition.empty:
            total_nutrition['proteins'] += nutrition['proteins'].values[0]
            total_nutrition['fats'] += nutrition['fats'].values[0]
            total_nutrition['carbohydrates'] += nutrition['carbohydrates'].values[0]
            total_nutrition['sugars'] += nutrition['sugars'].values[0]
    
    return total_nutrition

@app.route('/nutrition', methods=['POST'])
def nutrition():
    ingredients = request.json.get('ingredients', [])
    nutritional_info = get_nutritional_info(ingredients)
    
    return jsonify(nutritional_info)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
