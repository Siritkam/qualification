from flask import Flask
from flask import render_template, redirect


app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/')
def Error():
    return redirect ('/login')
    #return render_template('error.html')    


if __name__ == '__main__':
    app.run(debug=True)