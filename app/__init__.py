from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

#from flask.ext.login import LoginManager
#lm = LoginManager()
#lm.session_protection = 'strong'
#lm.init_app(app)
#lm.login_view = 'index'
from app import views, models
from config import basedir
import os
#from flask.ext.session import Session
#sess = Session()
#sess.init_app(app)



