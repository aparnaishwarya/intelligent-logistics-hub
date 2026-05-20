from flask import Flask, jsonify, request
import joblib
import numpy as np

from damage_detection.detect_damage import predict_damage
import os

app = Flask(__name__)

# Load trained model
model = joblib.load("models/sales_model.pkl")

# Health check
@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ML Service Running"
    })

# Predict future sales
@app.route('/predict-sales', methods=['POST'])
def predict_sales():

    data = request.json

    future_day = data.get("day")

    if future_day is None:
        return jsonify({
            "error": "Please provide day"
        }), 400

    prediction = model.predict(np.array([[future_day]]))

    return jsonify({
        "future_day": future_day,
        "predicted_sales": round(float(prediction[0]), 2)
    })


@app.route('/detect-damage', methods=['POST'])
def detect_damage():

    if 'image' not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400

    image = request.files['image']

    # Create upload folder if not exists
    os.makedirs("damage_detection/uploads", exist_ok=True)

    image_path = os.path.join(
        "damage_detection/uploads",
        image.filename
    )

    image.save(image_path)

    result = predict_damage(image_path)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)


