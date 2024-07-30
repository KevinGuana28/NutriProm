from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

INGREDIENT_SERVICE_URL = 'http://localhost:5001/predict'
NUTRITION_SERVICE_URL = 'http://localhost:5002/nutrition'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    response = requests.post(INGREDIENT_SERVICE_URL, files={'image': file})
    ingredients = response.json().get('ingredients', [])

    response = requests.post(NUTRITION_SERVICE_URL, json={'ingredients': ingredients})
    nutritional_info = response.json()
    
    return jsonify({
        'ingredients': ingredients,
        'nutritional_info': nutritional_info
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

