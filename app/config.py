from flask_sqlalchemy import SQLAlchemy
from pathlib import Path


SECRET_KEY = "jnnaldlsdfpor[qr[]qo23o-23olksmlvm"

SQLALCHEMY_TRACK_MODIFICATIONS = True


basedir = Path(__file__).resolve().parent
SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir}/core.db'