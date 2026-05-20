import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Load dataset
df = pd.read_csv("../datasets/sales_data.csv")

# Features and labels
X = df[['day']]
y = df['sales']

# Train model
model = LinearRegression()
model.fit(X, y)

# Create models directory if not exists
os.makedirs("../models", exist_ok=True)

# Save trained model
joblib.dump(model, "../models/sales_model.pkl")

print("Model trained and saved successfully!")