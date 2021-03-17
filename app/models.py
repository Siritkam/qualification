from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_name = db.Column(db.String, unique=True, nulltable=False)
    u_password = db.Column(db.String, unique=False, nulltable=False)
    u_role = db.Column(db.String, nulltable=False)


def __repr__(self):
    return '<id и Пользователь {} {}'.format(self.id, self.u_name)