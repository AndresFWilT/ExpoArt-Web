# imports
from flask import Flask, render_template, request, redirect
from config import DevelopmentConfig
from jinja2 import Environment, FileSystemLoader
import os
app = Flask(__name__)

@app.route('/')
def init():
    return index()

@app.route('/index')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.config.from_object(DevelopmentConfig)
    app.run(debug=True)