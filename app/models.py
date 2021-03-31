from flask_sqlalchemy import SQLAlchemy
import app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    u_login = db.Column(db.String(128), unique=True)
    u_pass = db.Column(db.String(128), unique=False)
    u_name = db.Column(db.String(128), index=True, unique=True)
    u_mail = db.Column(db.String(128), index=True, unique=False)
    u_role = db.Column(db.String(20), index=True)
    
    def set_password(self, u_pass):
        self.u_pass = generate_password_hash(u_pass)

    def check_password_hash(self, u_pass):
        return check_password_hash(self.u_pass, u_pass)


def __repr__(self):
    return '<id и Пользователь {} {} {}'.format(self.id, self.u_login, self.u_role)