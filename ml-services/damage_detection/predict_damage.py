from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

model = load_model("models/cnn_damage_model.h5")

def predict_damage(img_path):

    img = image.load_img(img_path, target_size=(128,128))

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)

    img_array /= 255.0

    prediction = model.predict(img_array)

    if prediction[0][0] > 0.5:
        return {
            "status": "Damaged"
        }
    else:
        return {
            "status": "Normal"
        }