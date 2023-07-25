from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=data)

@app.route("/post/<blog_id>")
def blog_post(blog_id):
    return render_template("post.html", posts=data, id=int(blog_id))

if __name__ == "__main__":
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    app.run(debug=True)
