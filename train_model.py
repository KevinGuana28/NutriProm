import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory

# Cargar Food-101
dataset = image_dataset_from_directory(
    'path_to_food101/food-101/images',
    image_size=(224, 224),
    batch_size=32,
    validation_split=0.2,
    subset="training",
    seed=123
)
validation_dataset = image_dataset_from_directory(
    'path_to_food101/food-101/images',
    image_size=(224, 224),
    batch_size=32,
    validation_split=0.2,
    subset="validation",
    seed=123
)

# Construir y entrenar el modelo CNN
model = tf.keras.applications.ResNet50(
    input_shape=(224, 224, 3),
    weights=None,
    classes=101
)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(dataset, validation_data=validation_dataset, epochs=10)

# Guardar el modelo entrenado
model.save('ingredient_service/food101_model.h5')
