from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import joblib
from damage_detection.predict_damage import predict_damage
import os

app = Flask(__name__)

# Load model and scaler
model = load_model(
    "models/lstm_sales_model.keras",
    compile=False
)
scaler = joblib.load("models/scaler.pkl")

@app.route('/predict-sales', methods=['POST'])
def predict_sales():

    data = request.json

    sequence = data.get("sequence")

    if len(sequence) != 3:
        return jsonify({
            "error": "Sequence must contain 3 values"
        }), 400

    sequence = np.array(sequence).reshape(-1, 1)

    sequence = scaler.transform(sequence)

    X_test = np.array([sequence])

    prediction = model.predict(X_test)

    prediction = scaler.inverse_transform(prediction)

    return jsonify({
        "predicted_sales": round(float(prediction[0][0]), 2)
    })


@app.route('/detect-damage', methods=['POST'])
def detect_damage():

    if 'image' not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400

    file = request.files['image']

    upload_path = os.path.join(
        "damage_detection/uploads",
        file.filename
    )

    os.makedirs(
        "damage_detection/uploads",
        exist_ok=True
    )

    file.save(upload_path)

    result = predict_damage(upload_path)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)