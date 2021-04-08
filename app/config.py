from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
import psycopg2



SECRET_KEY = "jnnaldlsdfpor[qr[]qo23o-23olksmlvm"

SQLALCHEMY_TRACK_MODIFICATIONS = True

#ограничение на размер загружаемого файла
MAX_FILE_SIZE = 1024 * 1024 + 1

#basedir = Path(__file__).resolve().parent
#SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir}/core.db'

SQLALCHEMY_DATABASE_URI = f'postgresql://Admin:0990DoomMetal@localhost:5433/coredb'