# imports
from flask import Flask, render_template, request, redirect
from config import DevelopmentConfig
from jinja2 import Environment, FileSystemLoader
import os
app = Flask(__name__)

# endpoint for the app
@app.route('/')
def init():
    return index()

# endpoint for index
@app.route('/index')
def index():
    return render_template('index.html')

# endpoint for comunication
@app.route('/comunication')
def module_communication():
    return render_template('comunication.html')

# app start
if __name__ == '__main__':
    app.config.from_object(DevelopmentConfig)
    app.run(debug=True)