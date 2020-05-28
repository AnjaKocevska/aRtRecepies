
from flask import Flask, render_template, request, redirect, url_for
from .forms import RegistrationForm
from .models import User
#from . import app


@app.route('/')
@app.route('/index')
def index():

    form = RegistrationForm()
    form = LoginForm()
    return render_template("index.html.jinja2", form=form)

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
            'SELECT id FROM user WHERE username = ?', (email, )
        ).fetchone() is not None:
            error = 'User {} is already taken. '.format(email)

        if error is None:
            db.execute(
                'INSERT INTO user (email, password) VALUES (?, ?) ',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('/login')

       

    return redirect(url_for('/index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        user = User(form.email.data, form.password.data, form.remember.data)
    return redirect(url_for('index'))

#if __name__  == "__main__":
    #app.run(port=3000, debug=True)