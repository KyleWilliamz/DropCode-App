from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

application = Flask(__name__, instance_relative_config=True)
application.config.from_pyfile('config.py')
application.config['SECRET_KEY']
application.config['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(application)
migrate = Migrate(application, db)
login = LoginManager(application)
login.login_view = 'login'
login.login_message_category= 'info'

from website import routes, models