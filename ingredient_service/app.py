from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import cv2
import json

app = Flask(__name__)

# Cargar el modelo preentrenado
model = tf.keras.models.load_model('food101_model.h5')

# Cargar el mapeo de categorías a ingredientes
with open('category_to_ingredients.json', 'r') as f:
    category_to_ingredients = json.load(f)

# Convertir las clases de Food-101 a nombres de categorías
food101_classes = ['apple_pie', 'baby_back_ribs', 'baklava', ..., 'waffles']

def map_predictions_to_ingredients(predictions):
    predicted_class = np.argmax(predictions)
    category = food101_classes[predicted_class]
    ingredients = category_to_ingredients.get(category, [])
    return list(ingredients)

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224))  # Ajustar el tamaño según tu modelo
    img = np.expand_dims(img, axis=0)
    predictions = model.predict(img)
    
    ingredients = map_predictions_to_ingredients(predictions)
    
    return jsonify({
        'ingredients': ingredients
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
