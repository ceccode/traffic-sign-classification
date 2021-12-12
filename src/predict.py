from flask import Flask
from flask import request as request_f
from flask import jsonify

import pickle
from tensorflow import keras
import numpy as np
import os
from io import BytesIO
from urllib import request
from PIL import Image


def download_image(url):
    print(url)
    with request.urlopen(url) as url:
        f = BytesIO(url.read())

    img = Image.open(f)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img


def prepare_input(x):
    return x / 255.0


model_file = 'traffic-sign-model.h5'
model = keras.models.load_model(model_file)


app = Flask('income')


@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return 'up!'


@app.route('/predict', methods=['POST'])
def predict():
    url = request_f.get_json()['url']
    print(url)

    img = download_image(url)
    img = prepare_image(img, target_size=(32, 32))

    x = np.array(img)
    X = np.array([x])

    X = prepare_input(X)

    pred = model.predict(X)

    classes = [
        "Speed limit (20km/h)",
        "Speed limit (30km/h)",
        "Speed limit (50km/h)",
        "Speed limit (60km/h)",
        "Speed limit (70km/h)",
        "Speed limit (80km/h)",
        "End of speed limit (80km/h)",
        "Speed limit (100km/h)",
        "Speed limit (120km/h)",
        "No passing",
        "No passing for vehicles over 3.5 metric tons",
        "Right-of-way at the next intersection",
        "Priority road",
        "Yield",
        "Stop",
        "No vehicles",
        "Vehicles over 3.5 metric tons prohibited",
        "No entry",
        "General caution",
        "Dangerous curve to the left",
        "Dangerous curve to the right",
        "Double curve",
        "Bumpy road",
        "Slippery road",
        "Road narrows on the right",
        "Road work",
        "Traffic signals",
        "Pedestrians",
        "Children crossing",
        "Bicycles crossing",
        "Beware of ice/snow",
        "Wild animals crossing",
        "End of all speed and passing limits",
        "Turn right ahead",
        "Turn left ahead",
        "Ahead only",
        "Go straight or right",
        "Go straight or left",
        "Keep right",
        "Keep left",
        "Roundabout mandatory",
        "End of no passing",
        "End of no passing by vehicles over 3.5 metric tons"
    ]

    return jsonify(str(dict(zip(classes, pred[0]))))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
