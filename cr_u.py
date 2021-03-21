from getpass import getpass
import sys

from app import create_app
from app.models import User, db

app = create_app()
app.app_context().push()

with app.app_context():
    userlogin = input('Введите логин: ')
    username = input('Введите имя: ')
    usermail = input('Введите почту: ')

    if User.query.filter(User.u_login == userlogin).count():
        print('Такой пользователь уже существует')
        sys.exit(0)

    password = getpass('Введите пароль')
    password_repeat = getpass('Повторите пароль')

    if password != password_repeat:
        print('Пароли не совпадают')
        sys.exit(0)

new_user = User(u_login=userlogin, u_name=username, u_mail=usermail, u_role='Admin')
new_user.set_password(password)

db.session.add(new_user)
db.session.commit() 
print('Создан пользователь: id-{} {}'.format(new_user.id, new_user.u_name))