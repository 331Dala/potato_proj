import numpy as np
from fastapi import  FastAPI, File, UploadFile
import uvicorn
from io import BytesIO
from PIL import Image
import tensorflow as tf
import requests

app = FastAPI()

# dynamically use the latest version model.
endpoint = "http://localhost:8502/v1/models/potatoes_model:predict"



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
    img_batch = np.expand_dims(image, 0)

    json_data = {
        "instances": img_batch.tolist()
    }

    # try:
    #     response = requests.post(endpoint, json=json_data)
    #     response.raise_for_status()  # 检查响应状态码
    #     predictions = response.json()["predictions"]
    #     predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    #     return {"predicted_class": predicted_class}
    # except requests.exceptions.RequestException as e:
    #     return {"error": f"请求失败: {e}"}
    response = requests.post(endpoint, json=json_data)
    # pass
    prediction = np.array(response.json()["predictions"][0])

    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction)

    return {
        "class": predicted_class,
        "confidence": float(confidence)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)