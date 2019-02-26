from io import BytesIO

import json

import base64
import numpy as np
import cv2
from PIL import Image

import tensorflow as tf
from keras.models import load_model

from flask import Flask, render_template, request

app = Flask(__name__)

graph = tf.get_default_graph()

@app.route("/", methods=['GET', 'POST'])
def pati():
    prediction = ''
    if 'img' in request.form.keys():
        s = request.form['img']
        im = Image.open(BytesIO(base64.b64decode(s)))
        open_cv_image = np.array(im)
        open_cv_image = open_cv_image[:, :, ::-1].copy() 
        img = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
        img_resized = cv2.resize(img, (32, 32))
        input_im = np.reshape(img_resized, (1, 32, 32, 1))
        with graph.as_default():
            probs = model.predict(input_im)[0]
            prob_ind = np.argmax(probs)
            print(probs)
            print(prob_ind)
            prediction = chars[prob_ind]
    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    model = load_model('out/model.h5')
    # Load devanagari characters
    with open("data/external/dev-char.txt", encoding='utf-8') as f:
        chars = f.readline().split(',')
    app.run(debug=True)
