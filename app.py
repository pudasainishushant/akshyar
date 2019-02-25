from io import BytesIO

import json

import base64

import cv2
import numpy as np
from PIL import Image
from bokeh import model

from flask import Flask, render_template, request
from keras.engine.saving import load_model
from numpy.core.tests.test_einsum import chars

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def pati():
    if 'img' in request.form.keys():
        s = request.form['img']
        im = Image.open(BytesIO(base64.b64decode(s)))
        # a = np.array(im)
        # print(a.shape)
        open_cv_image = np.array(im)
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        img = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
        img_resized = cv2.resize(img, (32, 32))
        cv2.imwrite('last.png', img_resized)
        input_im = np.reshape(img_resized, (1, 32, 32, 1)) # Passing 1 image through singel channel
        print(input_im.shape)
        '''
        with graph.as_default():
            probs = model.predict(input_im)[0]
            prob_ind = np.argmax(probs) # max value index
            print(probs)
            print(prob_ind)
            prediction = chars[prob_ind]
        '''
    return render_template('index.html', prediction ='predicition')


if __name__ == '__main__':
    model = load_model('out/model.h5')
    # load devnagari characters
    with open("data/external/dev-char.txt", encoding ='utf-8') as f:
        chars = f.readline().split(',')
    app.run(debug=True)
