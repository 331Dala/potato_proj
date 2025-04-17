import numpy as np
from fastapi import  FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

# main.py didn't deploy on tf server. Just for testing
# main.py didn't deploy on tf server. Just for testing
# main.py didn't deploy on tf server. Just for testing
# main.py didn't deploy on tf server. Just for testing
# main.py didn't deploy on tf server. Just for testing

origins = [
    "http://localhost",
    "http://localhost:3000",
]
# CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model("../saved_models/1")

# prod_model = tf.keras.models.load_model("../saved_models/1")
# beta_model = tf.keras.models.load_model("../saved_models/2")
# Change it to use the tfserving docker.

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(
        file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    image_batch = np.expand_dims(image, 0)

    prediction = MODEL.predict(image_batch)

    predict_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])
    return {
        "class": predict_class,
        "confidence": float(confidence)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
