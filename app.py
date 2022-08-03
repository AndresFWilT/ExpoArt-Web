# imports
from flask import Flask, render_template, request, redirect
from config import DevelopmentConfig
from jinja2 import Environment, FileSystemLoader
import os
app = Flask(__name__)

# endpoint for the app view
@app.route('/')
def init():
    return index()

# endpoint for index view
@app.route('/index')
def index():
    return render_template('index.html')

# endpoint for addArtwork view
@app.route('/addArtwork')
def add_artwork_view():
    artist = ""
    artwork = ""
    return render_template('addArtwork.html', artist = artist, artwork= artwork)

# endpoint for addArtist view
@app.route('/addArtist')
def add_artist_view():
    return render_template('addArtist.html')

# endpoint for addTechnic view
@app.route('/addArtisticTechnic')
def add_artistic_technic_view():
    return render_template('addArtisticTechnic.html')

# endpoint for comunication
@app.route('/comunication')
def module_communication():
    return render_template('comunication.html')

# app start
if __name__ == '__main__':
    app.config.from_object(DevelopmentConfig)
    app.run(debug=True)