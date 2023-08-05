from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=data, date=now)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<id>")
def post(id):
    return render_template("post.html", id=int(id), posts=data, date=now)

response = requests.get("https://api.npoint.io/edc117cc51ba131a43c2")
data = response.json()
now = datetime.now().strftime("%B %d, %Y")
print(now)

if __name__ == "__main__":
    app.run(debug=True)