from flask import Flask, render_template, jsonify, request
from werkzeug.utils import secure_filename
from bson import json_util
from datetime import datetime
import pytz
import math
# from keras.models import model_from_json
# import tensorflow as tf
# import cv2
# import numpy as np
import os

if not os.path.exists('uploads'):
    os.mkdir('uploads')

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'JPG', 'JPEG']

# global model, graph, label_dictionary

# label_dictionary = {0: 'Early Blight', 1: 'Healthy', 2: 'Late Blight'}

# json_file = open('model/model.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# model = model_from_json(loaded_model_json)
# model.load_weights("model/model.h5")

# graph = tf.get_default_graph()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/image", methods = ['POST'])
def predict():
    image = request.files['file']
    extension = secure_filename(image.filename).split('.')[-1]
    if extension not in ALLOWED_EXTENSIONS:
        return jsonify({'status':False, 'message':'Image type not supported'})
    else:
        image_path = 'uploads/' + str(datetime.now()) + '.' + extension
        try:
            image.save(image_path)

            img = cv2.imread(image_path)
            output = cv2.resize(img, (256, 256)).copy()
            img = cv2.resize(img, (128, 128))
            img = img / 255
            with graph.as_default():
                proba = model.predict(img.reshape(-1, 128, 128, 3))
        except Exception as _:
            return jsonify({'status':False, 'message': 'Something went wrong!'})

        idx = np.argmax(proba)
        return jsonify({'status':True, 'message': label_dictionary[idx], 'score': str(np.max(proba) * 100)[:5] + "%"})

if __name__ == '__main__':
    app.run(debug=False)