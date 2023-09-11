from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import confidential as conf

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
WTF_CSRF_SECRET_KEY = 'movieappcsrfkey'
movie_search_url = "https://api.themoviedb.org/3/search/movie?query=Jack%20R&include_adult=true&language=en-US&page=1"
movie_search_url = "https://api.themoviedb.org/3/search/movie"

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-library.db"
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)


class EditForm(FlaskForm):
    new_rating = StringField(
        "Your rating out of 10 i.e. 7.5", validators=[DataRequired()])
    new_review = StringField(
        "Your review", validators=[DataRequired()])
    submit = SubmitField()


class AddForm(FlaskForm):
    movie_name = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    movies_ = db.session.execute(
        db.select(Movie).order_by(Movie.rating)).scalars().all()
    rank = 1
    for movie in movies_[::-1]:
        print(movie)
        movie.ranking = rank
        rank += 1
        db.session.commit()

    return render_template("index.html", movies=movies_)


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        movie = add_form.movie_name.data
        params = {"query": movie, "include_adult": True, "language": "en-US"}
        response = requests.get(
            movie_search_url, headers=conf.TMDB_HEADER, params=params).json()
        movies_ = response['results']
        return render_template("select.html", movies=movies_)
    if len(request.args) == 0:
        return render_template("add.html", form=add_form)
    else:
        title = request.args.get('name')
        year = request.args.get('year')
        description = request.args.get('description')
        poster = 'https://image.tmdb.org/t/p/original' + \
            request.args.get('img_url')
        print(title, year, description, poster)
        movie = Movie(title=title, year=year, description=description,
                      rating=0.0, ranking=-1, review="None", img_url=poster)
        with app.app_context():
            db.session.add(movie)
            db.session.commit()

        movie_id = db.session.execute(db.select(Movie).where(
            Movie.title == title and Movie.year == year)).scalars().all()[0].id
        return redirect(f"/edit?id={movie_id}")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get('id')
    movie = db.session.execute(db.select(Movie).where(
        Movie.id == id)).scalars().all()[0]
    edit_form = EditForm()

    if edit_form.validate_on_submit():
        rating = edit_form.new_rating.data
        review = edit_form.new_review.data
        movie.rating = rating
        movie.review = review
        db.session.commit()
        return redirect("/")

    return render_template("edit.html", form=edit_form, title=movie.title)


@app.route("/delete")
def delete():
    id = request.args.get('id')
    movie = db.session.execute(db.select(Movie).where(
        Movie.id == id)).scalars().all()[0]
    db.session.delete(movie)
    db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
