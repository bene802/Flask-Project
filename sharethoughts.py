from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import SignUpForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dd2f2f39f11dab2c8497833d5a0e9d38'
# secrect key used to protect forms against modifing cookies, cross-site request, html file "hidden_tag() is used for it"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
from models import User, Post


posts = [
    {
        'author': 'Oliver',
        'title': 'Thought1',
        'date': '2019-02-18',
        'content': "Hello World"
    },
    {
        'author': 'Mike',
        'title': 'Thought2',
        'date': '2019-02-19',
        'content': "Cool Place!"
    }
]


@app.route("/home")
def home():
    return render_template('home.html', title='home', thoughts=posts)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()  # create an instance of the form
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', title='signup', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'zetong@nyu.edu' and form.password.data == 'password':
            flash('Log in succefully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful, please check your email and password', 'danger')
    return render_template('login.html', title='login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
