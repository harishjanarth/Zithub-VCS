from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'market.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(r"storage\templates\new"), 'design')  # Set uploads outside Zithub
app.config['UPLOAD_MAIN_FOLDER'] = 'uploads_main/'
app.config['UPLOAD_BRANCH_FOLDER'] = 'uploads_branch/'
app.config['MAX_CONTENT_PATH'] = 1024 * 1024
app.config['SECRET_KEY'] = '0c77990db79efda646f7515e'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from storage import routes

# Create the uploads folder outside Zithub directory
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

if not os.path.exists(app.config['UPLOAD_MAIN_FOLDER']):
    os.makedirs(app.config['UPLOAD_MAIN_FOLDER'])

if not os.path.exists(app.config['UPLOAD_BRANCH_FOLDER']):
    os.makedirs(app.config['UPLOAD_BRANCH_FOLDER'])
