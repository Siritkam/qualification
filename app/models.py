from flask_sqlalchemy import SQLAlchemy
import app


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_name = db.Column(db.String, unique=True)
    u_password = db.Column(db.String, unique=False)
    u_role = db.Column(db.String)


def __repr__(self):
    return '<id и Пользователь {} {}'.format(self.id, self.u_name)