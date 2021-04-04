from getpass import getpass
import sys

from app import create_app
from app.models import User, db, Role

app = create_app()
app.app_context().push()

with app.app_context():
    userlogin = input('Введите логин: ')
    username = input('Введите имя: ')
    usermail = userlogin
    userrole = input('Введите роль пользователя (Admin, it, Accauntant, Recruiter, Supervisor)')

    if User.query.filter(User.u_login == userlogin).count():
        print('Такой пользователь уже существует')
        sys.exit(0)

    password = getpass('Введите пароль')
    password_repeat = getpass('Повторите пароль')

    if password != password_repeat:
        print('Пароли не совпадают')
        sys.exit(0)

new_user = User(u_login=userlogin, u_name=username, u_mail=usermail)
new_user.set_password(password)
new_role = Role(u_login=userlogin, u_role=userrole)

db.session.add(new_user, new_role)
db.session.commit() 
print('Создан пользователь: id-{} {} {}'.format(new_user.id, new_user.u_name, new_role.u_role))