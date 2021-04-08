from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, DateTime, Numeric
import app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

#Таблица пользователей
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(256), unique=False)
    name = db.Column(db.String(64), index=True, unique=False)
    mail = db.Column(db.String(64), index=True, unique=False)
    
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password, password)

#Таблица со списком доступов
class Accesses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(User.id), unique=True)
    user_role = db.Column(db.String(64), index=True, nullable=False)

#Таблица со списком контрагентов
class Contractors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contractor = db.Column(db.String(128), unique=True)


#Таблица статей ддс
class CashFlowCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_article = db.Column(db.String(64), nullable=False)

#Таблица фактических затрат
class Payments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_1c = db.Column(db.String(24), unique=True, nullable=False)
    id_contractor = db.Column(db.Integer, ForeignKey(Contractors.id), unique=True)
    id_article = db.Column(db.Integer, ForeignKey(CashFlowCategory.id), unique=True)
    fact_summ = db.Column(db.Numeric, nullable=False)
    date_payment = db.Column(db.DateTime, unique=False, nullable=False)


#Таблица планируемых затрат
class Planed_cost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planed_amount = db.Column(db.Numeric, nullable=False)
    id_article = db.Column(db.Integer, ForeignKey(Contractors.id))
    year = db.Column(db.DateTime, nullable=False)



def __repr__(self):
    return '<id и Пользователь {} {} {}'.format(self.id, self.login, self.user_role)