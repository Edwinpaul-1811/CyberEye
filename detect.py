import tensorflow as tf
from tensorflow.keras.preprocessing import image  # Correct import
import numpy as np

# Load pre-trained model
MODEL_PATH = "model/xception_deepfake_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

def preprocess_img(img_path):
    img = image.load_img(img_path, target_size=(299, 299))  # Xception input size
    img_array = image.img_to_array(img)  # Fix: image module should be used here
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize
    return img_array

def predict_deepfake(img_path):
    img_array = preprocess_img(img_path)
    prediction = model.predict(img_array)[0][0]  # Assuming output is a probability
    return "DeepFake" if prediction > 0.5 else "Real"
