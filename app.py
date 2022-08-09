# imports
from ensurepip import bootstrap
from flask import Flask, render_template, request, redirect, url_for, flash, session, redirect
from components.divulgation.ArtworkCreation import ArtworkCreation
from config import DevelopmentConfig
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from jinja2 import Environment, FileSystemLoader
import os
import psycopg2 
import psycopg2.extras
import re
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
bootstrap = Bootstrap(app)
FontAwesome(app)
app.secret_key = 'expoartweb-arquitectura'


# imports from modules
## databases
from components.dataBases.context.Operations import Operations
from components.dataBases.strategy.QueryExecutionVerifyConnection import QueryExecutionVerifyConnection
## divulgation
from components.divulgation.ArtistCreation import ArtistCreation
from components.divulgation.TechnicCreation import TechnicCreation
from components.divulgation.tableTemplateRender import tableTemplateRender
from components.divulgation.GalleryCreation import GalleryCreation

# global
UPLOAD_FOLDER = '/static/images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


## --------------------------- Endpoints for every module ------------------------------------

# endpoint for CRUD view (MODULE registration, divulgation)
@app.route('/crud')
def crud_view():
    return render_template('CRUDIndex.html')

## --------------------------- Divulgation Module ---------------------------------------------

# endpoint for the app view
@app.route('/')
def init():
    return index("")

# endpoint for index view
@app.route('/index')
def index(message):
    # create the gallery
    create_gallery = GalleryCreation('')
    gallery = create_gallery.create_gallery()
    if (gallery is None):
        message = "No hay obras registradas en el sistema"
        return render_template('index.html', message = message)
    else:
        return render_template('index.html',gallery = gallery, message = message)

# endpoint for view specific artwork
@app.route('/visualizeArtwork', methods=['POST'])
def visualize_artwork():
    if request.method == 'POST':
        view_artwork = GalleryCreation(request.form['artwork'])
        artwork_info = view_artwork.create_specific_artwork()
        print(type(artwork_info))
        return render_template('visualizeArtwork.html', artwork_info = artwork_info)

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

# endpoint for saveArtWork
@app.route('/publishArtwork',methods=['POST'])
def save_artwork():
    if request.method == 'POST':
        file = request.files['img']
        if file and allowed_file(file.filename):
            data = request.form.to_dict()
            create = ArtworkCreation(data,secure_filename(file.filename))
            message = create.save_all_tables_artwork(create.createArtwork())
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return index(message)
        else:
            message = "Tipo de archivo no permitido"
            return index(message)
    else:
        message = "Illegal Request method"
        return index(message)

# endpoint for saveArtist
@app.route('/saveArtist', methods=['POST'])
def save_artist():
    if request.method == 'POST':
        create = ArtistCreation(request.form)
        message = create.saveArtist(create.createArtist())
        return index(message)
    else:
        message = "Illegal Request method"
        return index(message)
        
# endpoint for saveArtisticTechnic
@app.route('/saveArtisticTechnic', methods=['POST'])
def save_artistic_technic():
    if request.method == 'POST':
        create = TechnicCreation(request.form)
        message = create.saveTechnic(create.createTechnic())
        return index(message)
    else:
        message = "Illegal Request method"
        return index(message)

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
        return index(message)

## --------------------------- Error Handling ---------------------------------------------

# endpoint for error404
@app.errorhandler(404)
def not_found(error):
    """ Método para error 404 """
    return render_template('errors/error404.html', error=error)

# endpoint for error500
@app.errorhandler(500)
def not_found(error):
    """ Método para error 500 """
    return render_template('errors/error500.html', error=error)

## --------------------------- Component Management ---------------------------------------------

# endpoint for Modulo Comunicación
@app.route('/ERROR_ModuloComunicacion_NoEncontrado')
def ModuloComunicacion():
    return render_template('errors/errorscomponents/errorcomunicationmodule.html')

# endpoint for Modulo Database
@app.route('/ERROR_ModuloDatabase_NoEncontrado')
def ModuloDatabase():
    return render_template('errors/errorscomponents/errordatabasemodule.html')

# endpoint for Modulo Divulgación
@app.route('/ERROR_ModuloDivulgacion_NoEncontrado')
def ModuloDivulgacion():
    return render_template('errors/errorscomponents/errordivulgationmodule.html')

# endpoint for Modulo Opinion
@app.route('/ERROR_ModuloOpinion_NoEncontrado')
def ModuloOpinion():
    return render_template('errors/errorscomponents/erroropinionmodule.html')

# endpoint for Modulo Registro
@app.route('/ERROR_ModuloRegistro_NoEncontrado')
def ModuloRegistro():
    return render_template('errors/errorscomponents/errorregistrationmodule.html')

# endpoint for Modulo Usuarios UD
@app.route('/ERROR_ModuloUsuariosUD_NoEncontrado')
def ModuloUsuariosUD():
    return render_template('errors/errorscomponents/errorUDusersmodule.html')



## --------------------------- Registration Module ---------------------------------------------

DB_HOST = "localhost"
DB_NAME ="expoart"
DB_USER ="postgres"
DB_PASS= "1234"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

## --------------------------- Beggining Role Management --------------------------------------------

## -------------- Persona externa -------------- 

# endpoint for index view Persona Externa
@app.route('/vistaPersonaExterna')
def vistaPersonaExterna():
    # Check if user is loggedin
    if 'loggedin' in session and session['type'] == "Persona Externa":
    
        # User is loggedin show them the home page
        return render_template('vistaPersonaExterna.html', id_user=session['id_user'])
    # User is not loggedin redirect to login page
    return index('message')


## -------------- Estudiante y Docente UD -------------- 

# endpoint for index view Estudiante y Docente UD


@app.route('/vistaPersonaUD')
def vistaPersonaUD():
    # Check if user is loggedin
    if 'loggedin' in session and (session['type'] == "Estudiante UD" or session['type'] == "Docente UD"):
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        s = "SELECT * FROM ideas"
        cur.execute(s) # Execute the SQL
        list_ideas = cur.fetchall()
        return render_template('vistaPersonaUD.html', list_ideas = list_ideas)
    elif 'loggedin' in session:
    # User is not loggedin redirect to login page
        return index("")
    else:
        return render_template('login.html')

@app.route('/add_idea', methods=['POST'])
def add_idea():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        ideas_title = request.form['ideas_title']
        ideas_desc = request.form['ideas_desc']
        ideas_phase = request.form['ideas_phase']
        cur.execute("INSERT INTO ideas (ideas_title, ideas_desc, ideas_phase) VALUES (%s,%s,%s)", (ideas_title, ideas_desc, ideas_phase))
        conn.commit()
        flash('Idea agregada con exito')
        return redirect(url_for('vistaPersonaUD'))

@app.route('/edit/<id_ideas>', methods = ['POST', 'GET'])
def get_employee(id_ideas):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM ideas WHERE id_ideas = %s', (id_ideas))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', ideas = data[0])
 
@app.route('/update/<id_ideas>', methods=['POST'])
def update_ideas(id_ideas):
    if request.method == 'POST':
        ideas_title = request.form['ideas_title']
        ideas_desc = request.form['ideas_desc']
        ideas_phase = request.form['ideas_phase']
        
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE ideas
            SET ideas_title = %s,
                ideas_desc = %s,
                ideas_phase = %s
            WHERE id_ideas = %s
        """, (ideas_title, ideas_desc, ideas_phase, id_ideas))
        flash('Idea actualizada con exito!')
        conn.commit()
        return redirect(url_for('vistaPersonaUD'))
 
@app.route('/delete/<string:id_ideas>', methods = ['POST','GET'])
def delete_ideas(id_ideas):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM ideas WHERE id_ideas = {0}'.format(id_ideas))
    conn.commit()
    flash('Idea eliminada con exito!')
    return redirect(url_for('vistaPersonaUD'))

## -------------- ADMIN -------------- 



## --------------------------- Finish Role Management --------------------------------------------


@app.route('/register', methods=['GET', 'POST'])
def register():
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


    # Check if "id_user", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'id_user' in request.form and 'password' in request.form and 'email_user' in request.form:
        # Create variables for easy access
        id_user = request.form['id_user']
        id_doc = request.form['id_doc']
        name_user = request.form['name_user']
        lastname_user = request.form['lastname_user']
        password = request.form['password']
        email_user = request.form['email_user']
        type = request.form['type']

        _hashed_password = generate_password_hash(password)
 
        #Check if account exists using MySQL
        cursor.execute('SELECT * FROM users WHERE id_user = %s', (id_user,))
        account = cursor.fetchone()
        print(account)
        
        # If account exists show error and validation checks
        if account:
            flash('La cuenta ya existe!')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email_user):
            flash('Dirección de email invalida!')
        elif not id_user or not password or not email_user:
            flash('Por favor diligencia el formulario!')
        else:
            # Account doesnt exists and the form data is valid, now insert new account into users table
            cursor.execute("INSERT INTO users (id_user, id_doc, name_user, lastname_user, password, email_user, type) VALUES (%s,%s,%s,%s,%s,%s,%s)", (id_user, id_doc, name_user, lastname_user, _hashed_password, email_user, type))
            conn.commit()
            flash('Su registro fue exitoso!')
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        flash('Por favor diligencia el formulario!')
    # Show registration form with message (if any)
    
    return render_template('register.html')

# endpoint for log in

@app.route('/login', methods=['GET', 'POST'])
def login():

    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    # Check if "id_user" and "password" POST requests exist (user submitted form)
    if request.method == 'POST':
        id_user = request.form['id_user']
        password = request.form['password']
        type = request.form['type']
        print(password)
 
        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM users WHERE id_user = %s', (id_user,))
        # Fetch one record and return result
        account = cursor.fetchone()
 
        if account:
            password_rs = account['password']
            print(password_rs)
            # If account exists in users table in out database
            if check_password_hash(password_rs, password):
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id_user'] = account['id_user']
                session['id_user'] = account['id_user']
                session['type'] = account['type']
                # Redirect to vista persona externa
                return index("logueado")
            else:
                # Account doesnt exist or username/password incorrect
                flash('Documento o password invalido')
        else:
            # Account doesnt exist or username/password incorrect
            flash('Documento o password invalido')


    return render_template('login.html')

# endpoint for logout
@app.route('/logoutPersonaExterna')
def logoutPersonaExterna():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id_user', None)
   session.pop('id_user', None)
   session.pop('type', None)
   # Redirect to login page
   return index('Se ha deslogeado con exito!')

# endpoint for profile Persona Externa
@app.route('/profilePersonaExterna')
def profilePersonaExterna():
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    # Check if user is loggedin
    if 'loggedin' in session and session['type'] == "Persona Externa":
        cursor.execute('SELECT * FROM users WHERE id_user = %s', [session['id_user']])
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profilePersonaExterna.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

## --------------------------- UD Users Module --------------------------------------------





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
    return index(message)

## -----------------------------------------------------------------------------------------------

#service for saving files
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# app start
if __name__ == '__main__':
    app.config.from_object(DevelopmentConfig)
    app.run(debug=True)

