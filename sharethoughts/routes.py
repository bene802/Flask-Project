from flask import render_template, url_for, flash, redirect, request
from sharethoughts import app, db, bcrypt
from sharethoughts.forms import SignUpForm, LoginForm, UpdateAccountForm
from sharethoughts.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


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


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='home', thoughts=posts)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignUpForm()  # create an instance of the form
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created succefully!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', title='signup', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            flash('Login unsuccessful, please check your email and password', 'danger')
    return render_template('login.html', title='login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    image = url_for('static', filename='images/' + current_user.image_file)
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        flash('You have updated your account!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':  # put original info into the table
        form.username.data = current_user.username
    return render_template('account.html', title='Account', image=image, form=form)
