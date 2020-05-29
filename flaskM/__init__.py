import os

from flask import Flask, render_template, request, redirect, url_for, session
from .forms import RegistrationForm, LoginForm
from .models import User
from .db import get_db 
from werkzeug.security import check_password_hash, generate_password_hash



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='7b0d9fe238977766d6ee2474585647cd',
        DATABASE=os.path.join(app.instance_path, 'site.sqlite'),
    )
    @app.route('/')
    @app.route('/index')
    def index():

        registration_form = RegistrationForm()
        login_form = LoginForm()

        #if session['user_id']:
          #  user_id = session['user_id']
           # print(user_id)
           # db = get_db()
            #email = db.execute("SELECT email FROM user WHERE id = ?", (user_id)).fetchone()

        return render_template("index.html.jinja2", registration_form=registration_form, login_form=login_form)

    @app.route("/glass")
    def glass():
        return render_template("glass.html.jinja2")
    
    @app.route("/plastic")
    def plastic():
        return render_template("plastic.html.jinja2")

    @app.route("/recepie")
    def recepie():
        return render_template("recepie.html.jinja2")
    
    @app.route("/recepie2")
    def recepie2():
        return render_template("recepie2.html.jinja2")

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegistrationForm(request.form)
        if request.method == 'POST':
            user = User(form.name.data, form.surname.data, form.email.data, form.password.data)
            db = get_db()
            error = None

            if not user.email:
                error = 'Email required'
            elif not user.password:
                error = 'Password required'
            elif db.execute(
                'SELECT id FROM user WHERE email = ?', (user.email, )
            ).fetchone() is not None:
                error = 'User {} is already taken. '.format(user.email)
                
            print(error)

            if error is None:
                db.execute(
                    'INSERT INTO user (email, password) VALUES (?, ?) ',
                    (user.email, generate_password_hash(user.password))
                )
                db.commit()
                return redirect(url_for('login'))
        
        return redirect(url_for('index'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm(request.form)
        if request.method == 'POST':

            email = form.email.data
            password = form.password.data

            db = get_db()
            error = None

            user = db.execute(
                'SELECT * FROM user WHERE email = ?', (email,)
            ).fetchone()

            if email is None:
                error = 'Incorrect email'
            elif not check_password_hash(user['password'],password):
                error = 'Incorect Password'
            
            if error is None:
                session.clear()
                session['user_id'] = user['id']
                return redirect(url_for('index'))
            #flash(error)
        #return render_template('login')



        """ if not email or not password:
          error = "email and password required"
        else:

           user = User(form.email.data, form.password.data, form.remember.data) """
        return redirect(url_for('index'))
    
    
    #for the config.py
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    db.init_app(app)

    return app