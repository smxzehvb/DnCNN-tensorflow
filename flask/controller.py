
from flask import Flask, render_template, request, redirect
import compute
import sys, os


app = Flask(__name__)



app.images_list =[]

@app.route('/')
def show_images():
    nimages, images_orig, images_denoise = compute.get_images_dir('/home/ubuntu/DnCNN-tensorflow/test/')
    return render_template('view.html', n=nimages, orig=images_orig, denoise=images_denoise)





if __name__ == '__main__':
    app.run(debug=True, port=8888, host='0.0.0.0')

