from getpass import getpass
import sys

from app import create_app
from app.models import User, db, Accesses

app = create_app()
app.app_context().push()
#добавит в функцию
with app.app_context():
    userlogin = input('Введите логин: ')
    username = input('Введите имя: ')
    usermail = userlogin
    userrole = input('Введите роль пользователя (Admin, it, Accauntant, Recruiter, Supervisor)')

    if User.query.filter(User.login == userlogin).count():
        print('Такой пользователь уже существует')
        sys.exit(0)

    password = getpass('Введите пароль')
    password_repeat = getpass('Повторите пароль')

    if password != password_repeat:
        print('Пароли не совпадают')
        sys.exit(0)

new_user = User(login=userlogin, name=username, mail=usermail)
new_user.set_password(password)


db.session.add(new_user)
db.session.commit()

new_role = Accesses(user_id=User.id, user_role=userrole)
db.session.add(new_role)
db.session.commit()
print('Создан пользователь: id-{} {} {}'.format(new_user.id, new_user.name, new_role.user_role))