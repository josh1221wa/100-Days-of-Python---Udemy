
'''In Flask we need to start the server manually. This is acheived by setting the FLASK_APP environment variable to the name of the file containing the Flask app. Then we can run the server using the "flask run" command.'''

from flask import Flask

app = Flask(__name__)       # create an app instance
# __name__ is a special python attribute that prints the current function or module name

@app.route("/")
#This part is called a decorator. It is used to tell Flask what URL should trigger the function.

def hello():
    return "Hello, World!"

@app.route("/bye")
def bye():
    return "Bye!"

if __name__ == "__main__":
    app.run()

'''This method of running avoids the need to set the FLASK_APP environment variable and also start the server manually. This is what most Flask programs may have.'''

