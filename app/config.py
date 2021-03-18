import os
import app 
from flask_sqlalchemy import SQLAlchemy


from pathlib import Path
basedir = Path(__file__).resolve().parent
SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir}/app.db'