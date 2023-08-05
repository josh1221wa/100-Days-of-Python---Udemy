from flask import Flask, render_template, request
import requests
import confidential
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", success=False)
    else:
        print(request.form['name'], request.form['email'], request.form['phone'], request.form['message'])
        sendmail(request.form['name'], request.form['email'], request.form['phone'], request.form['message'])
        return render_template("contact.html", success=True)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

def sendmail(name, email, phone, message):
    body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    my_email = confidential.MAIL_ID
    password = confidential.PASSWORD
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:New User\n\n{body}")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
