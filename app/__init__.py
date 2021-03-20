from flask import Flask, render_template, redirect, flash, url_for
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from app.models import db, User
from app.forms import LoginForm

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
            return redirect(url_for('/'))

        login_form = LoginForm()
        return render_template('login.html', form=login_form)

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter(User.u_login == form.userform.data).first()
            if user and user.check_password_hash(form.passform.data):
                login_user(user)
                #flash('Вы вошли на сайт')
                return redirect(url_for('control'))

        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('login'))


    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('login'))

    @app.route('/control')
    def control():
        form1 = logout_user()
        return render_template('control.html', form='logout_user')
 
    return app