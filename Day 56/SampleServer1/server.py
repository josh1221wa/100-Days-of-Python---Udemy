from flask import Flask, render_template

# Since flask is a framework it has its rules when it comes to rendering files and stuff and any templates we have must be kept in a folder called templates. 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("angela.html")
# This won't render any images or any css files as again as per Flask rules all static files such as images or css files have to be put in a folder called static

if __name__ == "__main__":
    app.run(debug=True)