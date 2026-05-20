from flask import Flask, jsonify, request
import joblib
import numpy as np

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

if __name__ == '__main__':
    app.run(debug=True)