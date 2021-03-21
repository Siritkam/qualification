from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    #логин пользователя
    userform = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    passform = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})

class logout_user(FlaskForm):
    submit_logout = SubmitField("Выйти", render_kw={"class": "btn btn-primary"})