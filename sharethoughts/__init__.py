from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dd2f2f39f11dab2c8497833d5a0e9d38'
# secrect key used to protect forms against modifing cookies, cross-site request, html file "hidden_tag() is used for it"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #login_required page
login_manager.login_message_category = 'info'  # set color to blue


from sharethoughts import routes
