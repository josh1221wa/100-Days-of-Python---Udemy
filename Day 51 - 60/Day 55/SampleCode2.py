# In flask, all the text that we return is put in the body tag of the html file. This means that we can use html tags to format our text.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

def bolden(function):
    def wrapper():
        return '<b>' + function() + '</b>'
    return wrapper

def emphasis(function):
    def wrapper():
        return '<em>' + function() + '</em>'
    return wrapper

def underline(function):
    def wrapper():
        return '<u>' + function() + '</u>'
    return wrapper

@app.route('/bye')
@bolden
@emphasis
@underline
def bye():
    return "Bye!"


if __name__ == '__main__':
    app.run(debug=True)