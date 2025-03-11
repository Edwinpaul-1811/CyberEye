from flask import Flask, render_template, request, jsonify
import os
from detect import predict_deepfake  # Import detection function

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect_deepfake():
    if "image" not in request.files:
        return jsonify({"message": "No image uploaded"}), 400

    image_file = request.files["image"]
    img_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(img_path)

    # Predict if the image is DeepFake or Real
    result = predict_deepfake(img_path)
    
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
