from flask import Flask, render_template, request
from keras.models import load_model
import os
import cv2 
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'static/img/input/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_PATH'] = 16 * 1024 * 1024
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1

model = load_model('Model/Outputs/finalModel.h5')


@app.route('/')
def ault():
    return render_template('index.html')

@app.route('/home', methods = ['POST'])
def home():
    img = request.files['image']
    img.save('static/img/input/0.jpg')

    img = cv2.imread('static/img/input/0.jpg')
    img1 = cv2.resize(img,(30,30))
    image = np.expand_dims(img1, axis=0)
    img = np.array(image)
    pred = model.predict_classes([image])[0]
    clas = pred+1
    return render_template('pred.html',clas=clas)


if __name__ == "__main__":
    app.run(debug=True)


