from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    #логин пользователя
    userform = StringField('', validators=[DataRequired()], render_kw={"class": "form-control"})
    passform = PasswordField('', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})

class logout_user(FlaskForm):
    submit_logout = SubmitField("Выйти", render_kw={"class": "btn btn-lg btn-primary btn-block"})