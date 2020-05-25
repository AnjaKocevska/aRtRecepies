
from flask import Flask, render_template, request, redirect, url_for
from forms import RegistrationForm
from models import User
#from app import app
app = Flask(__name__)


app.config['SECRET_KEY'] = '7b0d9fe238977766d6ee2474585647cd'



@app.route('/')
@app.route('/index')
def index():

    form = RegistrationForm()
    return render_template("index.html.jinja2", form=form)

@app.route("/bottles")
def bottles():
    return render_template("bottles.html.jinja2")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        user = User(form.name.data, form.surname.data, form.email.data, form.password.data)
       

    return redirect(url_for('index'))

if __name__  == "__main__":
    app.run(port=3000, debug=True)