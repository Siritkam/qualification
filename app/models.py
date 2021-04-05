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
    
    
    def set_password(self, u_pass):
        self.u_pass = generate_password_hash(u_pass)

    def check_password_hash(self, u_pass):
        return check_password_hash(self.u_pass, u_pass)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), unique=True)
    u_role = db.Column(db.String(64), index=True)


#class Dds(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    articles = db.Column(db.String(64), unique=True)
#    plan_costs = db.Column(db.Float)
#    fact_costs = db.Column(db.Float)
#    sum_devi = db.Column(db.Float)


#class Results(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    january = db.Column(db.Float)
#    february = db.Column(db.Float)
#    march = db.Column(db.Float)
#    april = db.Column(db.Float)
#    may = db.Column(db.Float)
#    june = db.Column(db.Float)
#    july = db.Column(db.Float)
#    august = db.Column(db.Float)
#    september = db.Column(db.Float)
#    october = db.Column(db.Float)
#    november = db.Column(db.Float)
#    december = db.Column(db.Float)
    

def __repr__(self):
    return '<id и Пользователь {} {} {}'.format(self.id, self.u_login, self.u_role)