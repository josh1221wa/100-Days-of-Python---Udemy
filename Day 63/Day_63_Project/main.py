from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()
    db.session.commit()


@app.route('/')
def home():
    book_data = db.session.execute(db.select(Books)).scalars().all()
    return render_template("index.html", library=book_data)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            db.session.add(Books(
                title=request.form['bookname'], author=request.form['author'], rating=request.form['rating']))
            db.session.commit()
        return redirect("/")
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get('id')
    book_ = db.session.execute(
        db.select(Books).where(id == Books.id)).scalars().all()[0]
    if request.method == "GET":
        return render_template("edit.html", book=book_)
    else:
        book_.rating = request.form['new_rating']
        db.session.commit()
        return redirect("/")


@app.route("/delete", methods=["GET"])
def delete():
    id = request.args.get('id')
    book_ = db.session.execute(
        db.select(Books).where(id == Books.id)).scalars().all()[0]
    db.session.delete(book_)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
