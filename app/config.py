from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

SQLALCHEMY_TRACK_MODIFICATIONS = True
basedir = Path(__file__).resolve().parent
SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir}/app2.db'