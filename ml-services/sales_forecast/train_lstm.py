import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.models import load_model
import joblib
import os

# Load dataset
df = pd.read_csv("../datasets/sales_data.csv")

dataset = df.values

# Normalize data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

# Create sequences
X = []
y = []

sequence_length = 3

for i in range(sequence_length, len(scaled_data)):
    X.append(scaled_data[i-sequence_length:i, 0])
    y.append(scaled_data[i, 0])

X = np.array(X)
y = np.array(y)

# Reshape for LSTM
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Build LSTM model
model = Sequential()

model.add(LSTM(units=50, return_sequences=True,
               input_shape=(X.shape[1], 1)))

model.add(LSTM(units=50))

model.add(Dense(1))

model.compile(
    optimizer='adam',
    loss='mean_squared_error'
)

# Train model
model.fit(X, y, epochs=50, batch_size=1)

# Create models directory
os.makedirs("../models", exist_ok=True)

# Save model
model.save("../models/lstm_sales_model.keras")

# Save scaler
joblib.dump(scaler, "../models/scaler.pkl")

print("LSTM model trained successfully!")