from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

# It gives the relative path to the database which will be stored in the instance folder of the app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
# This is to initialize the SQLAlchemy extension in the application
db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)

book1 = Books(id=1, title="Harry Potter", author="J.K. Rowling", rating=9.3)

with app.app_context():     # This is to manually create an app context
    # db.create_all()
    # db.session.add(book1)
    result = db.session.execute(db.select(Books).order_by(Books.title))
    print(result.scalars())
    db.session.commit()