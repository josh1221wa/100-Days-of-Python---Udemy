from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/guess/<name>")
def result(name):
    name = name.title()
    age = requests.get(f"https://api.agify.io/?name={name}").json()["age"]
    gender = requests.get(f"https://api.genderize.io/?name={name}").json()["gender"]
    return render_template("index.html", name=name, age=age, gender=gender)

@app.route("/blog")
def blog():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    posts = response.json()
    return render_template("blog.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)