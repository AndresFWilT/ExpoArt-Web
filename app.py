# imports
from flask import Flask, render_template, request, redirect
from config import DevelopmentConfig
from jinja2 import Environment, FileSystemLoader
import os
app = Flask(__name__)

# imports from modules
## databases
from components.dataBases.context.Operations import Operations
from components.dataBases.strategy.QueryExecutionVerifyConnection import QueryExecutionVerifyConnection
## divulgation
from components.divulgation.ArtistCreation import ArtistCreation
from components.divulgation.TechnicCreation import TechnicCreation
from components.divulgation.tableTemplateRender import tableTemplateRender


## --------------------------- Endpoints for every module ------------------------------------

# endpoint for CRUD view (MODULE registration, divulgation)
@app.route('/crud')
def crud_view():
    return render_template('CRUDIndex.html')

## --------------------------- Divulgation Module ---------------------------------------------

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
    # names from artist
    createArtist = ArtistCreation("")
    artist = createArtist.getArtistNames()
    # titles from technic
    createTechnics = TechnicCreation("")
    technic = createTechnics.getTechnicTitles()
    return render_template('addArtwork.html', artist = artist, technic= technic)

# endpoint for addArtist view
@app.route('/addArtist')
def add_artist_view():
    return render_template('addArtist.html')

# endpoint for addTechnic view
@app.route('/addArtisticTechnic')
def add_artistic_technic_view():
    return render_template('addArtisticTechnic.html')

# endpoint for saveArtist
@app.route('/saveArtist', methods=['POST'])
def save_artist():
    if request.method == 'POST':
        create = ArtistCreation(request.form)
        message = create.saveArtist(create.createArtist())
        return render_template('index.html',message = message)
    else:
        message = "Illegal Request method"
        return render_template('index.html',message = message)
        
# endpoint for saveArtisticTechnic
@app.route('/saveArtisticTechnic', methods=['POST'])
def save_artistic_technic():
    if request.method == 'POST':
        create = TechnicCreation(request.form)
        message = create.saveTechnic(create.createTechnic())
        return render_template('index.html',message = message)
    else:
        message = "Illegal Request method"
        return render_template('index.html',message = message)

# endpoint for render template view tables (artist, artisticTechnic, artwork)
@app.route('/viewDivulgationDataTables', methods=["POST"])
def view_divulgation_data_tables():
    if request.method == 'POST':
        table_render = tableTemplateRender(request.form)
        template, data = table_render.render_template()
        message = ""
        return render_template(template, message = message, data = data)
    else:
        message = "Illegal Request method"
        return render_template('index.html',message = message)

## --------------------------- Communication Module --------------------------------------------

# endpoint for communication
@app.route('/communication')
def module_communication():
    return render_template('communication.html')

## --------------------------- DataBase Module -------------------------------------------------

# endpoint to verify dataBaseConnection
@app.route('/dataBaseConnection')
def prove_database_connection():
    # Parameters (strategy class, data)
    EQSA = Operations(QueryExecutionVerifyConnection(),{''})
    # Data from the query executed
    message = EQSA.save()
    # rendering template
    return render_template('index.html',message = message)

## -----------------------------------------------------------------------------------------------

# app start
if __name__ == '__main__':
    app.config.from_object(DevelopmentConfig)
    app.run(debug=True)