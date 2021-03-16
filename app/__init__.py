import os
from flask import Flask, render_template, redirect
from app.models import db
#ициниализируем Flask-приложение
def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLAlchemy_DATABASE_URL = 'sqlite:///'+ os.path.join(basedir, '..', 'app.db')
    db.init.app(app)

    @app.route('/login')
    def login():
        return render_template('login.html')


    @app.route('/')
    def Error():
        #return render_template('error.html')    
        return redirect ('/login')

        
return app