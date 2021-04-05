from flask import Flask, render_template, redirect, flash, url_for, request
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from app.models import db, User, Role
from app.forms import LoginForm
from werkzeug.utils import secure_filename
from app.config import MAX_FILE_SIZE

#ициниализируем Flask-приложение
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    #return app
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        return render_template('index.html')
              
        #return redirect ('/login')


    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            redirect_path = request.args.get('next', '/')
            return redirect(redirect_path)
        
        login_form = LoginForm()
        return render_template('login.html', form=login_form)
        
#помнить про request
    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        #role = Role.query.u_role
        form_user, form_pass = form.userform.data, form.passform.data
        
        if form.validate_on_submit():
            user = User.query.filter_by(u_login = form_user).first()

        if user and user.check_password_hash(form_pass):
            login_user(user)
            #flash('Вы вошли на сайт')
            return redirect(url_for('control'))
        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('login'))


    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))

    @app.route('/control')
    @login_required
    def control():
        return render_template('control.html')
    

    @app.route('/dit')
    @login_required
    def dit():
        return render_template('dit.html')
 

    @app.route('/drp')
    @login_required
    def drp():
        return render_template('drp.html')
 
    return app