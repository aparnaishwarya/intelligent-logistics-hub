import pandas as pd
import logging
import os

# Create logs directory if not exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/cleaner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    # Read CSV
    df = pd.read_csv("sample_sales.csv")

    logging.info("CSV file loaded successfully")

    print("\nOriginal Data:")
    print(df)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')

    df['price'] = df['price'].fillna(0)
    df['quantity'] = df['quantity'].fillna(0)

    # Standardize date format
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Remove rows with invalid dates
    df = df.dropna(subset=['date'])

    # Format date
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')

    # Create cleaned directory
    os.makedirs("cleaned", exist_ok=True)

    # Save cleaned file
    output_path = "cleaned/cleaned_sales.csv"
    df.to_csv(output_path, index=False)

    logging.info("Cleaned CSV saved successfully")

    print("\nCleaned Data:")
    print(df)

    print(f"\nCleaned file saved at: {output_path}")

except Exception as e:
    logging.error(f"Error occurred: {e}")
    print("An error occurred:", e)