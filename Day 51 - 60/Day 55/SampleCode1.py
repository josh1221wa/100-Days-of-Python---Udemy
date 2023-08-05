# We can use variable rules in Flask to get the path the user enters in a variable and use it in our code.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def start():
    return f"Hello!"

@app.route("/<name>")
# This is a variable rule. The part of the URL enclosed in < > is a variable. The function will receive the variable as a parameter.
def greet(name):
    return f"Hello, {name}!"

# You can also specify data types for the variable rules. For example, if you want the variable to be an integer, you can do this:
@app.route("/<int:number>")
def print_number(number):
    return f"The number is {number}"


if __name__ == "__main__":
    app.run(debug=True)    # debug mode is enabled, it will automatically reload for code changes and show errors