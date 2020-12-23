from flask import Flask, render_template
# from keras.models import load_model
import os

uploadDir = 'static/img/input'
allowedExt = {'png'}
app = Flask(__name__)

# model = load_model('Model/Outputs/finalModel.h5')


@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


