from PIL import Image
import numpy as np

def predict_damage(image_path):

    # Open image
    image = Image.open(image_path)

    # Resize image
    image = image.resize((100, 100))

    # Convert to numpy array
    image_array = np.array(image)

    # Simple brightness-based dummy logic
    avg_pixel = image_array.mean()

    # Fake prediction logic
    if avg_pixel < 100:
        return {
            "status": "Damaged",
            "confidence": 88.5
        }
    else:
        return {
            "status": "Not Damaged",
            "confidence": 92.1
        }