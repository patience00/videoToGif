from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from FrameToGif import FrameToGif

import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/upload'


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        print(request.files)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        f.save(filepath)
        FrameToGif.videoToGif(filepath, 'C:/Users/Administrator/Pictures/', 200, 20, 200, 20)
        FrameToGif.jpgToGif(filepath, 'C:/Users/Administrator/Pictures/')
        os.remove(filepath)

        return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("9000"), debug=True)
