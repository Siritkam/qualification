from flask import Flask, render_template, redirect
from app.models import db
#ициниализируем Flask-приложение
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)


    @app.route('/')
    def Error():
        #return render_template('error.html')    
        return redirect ('/login')


    @app.route('/login')
    def login():
        return render_template('login.html')


    @app.route('/control')
    def control():
        return render_template('control.html')
 
    return app