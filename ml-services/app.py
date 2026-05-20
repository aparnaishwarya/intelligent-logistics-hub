from flask import Flask, jsonify, request

app = Flask(__name__)

# Health check route
@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ML Service Running"
    })

# Simple prediction route
@app.route('/predict-sales', methods=['POST'])
def predict_sales():

    data = request.json

    sales = data.get("sales", [])

    if not sales:
        return jsonify({
            "error": "No sales data provided"
        }), 400

    # Simple average prediction
    prediction = sum(sales) / len(sales)

    return jsonify({
        "predicted_sales": round(prediction, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)