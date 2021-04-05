from app import db, create_app
import psycopg2
from flask_sqlalchemy import SQLAlchemy


db.create_all(app=create_app())
def create_connection():
    connection = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
    )

create_connection()