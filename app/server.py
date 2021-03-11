from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('auth.html')


@app.route('/error')
def Error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)