import os
import app 
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLAlchemy_DATABASE_URl = f"sqlite:///{os.path.abspath(os.path.dirname(__file__))}, app.db"