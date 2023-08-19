from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)
API_KEY = "TopSecretKey"


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


# with app.app_context():
#     db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route("/random", methods=["GET"])
def random_cafe():
    index = random.randrange(1, 22)
    random_cafe = db.session.execute(db.select(Cafe).where(
        Cafe.id == index)).scalars().all()[0]
    cafe_dict = {}
    for column in random_cafe.__table__.columns:
        cafe_dict[column.name] = getattr(random_cafe, column.name)
    return jsonify(cafe=cafe_dict)


@app.route("/all", methods=["GET"])
def get_all():
    all_cafes = db.session.execute(
        db.select(Cafe).order_by(Cafe.id)).scalars().all()
    cafes_list = []
    for cafe in all_cafes:
        cafe_dict = {}
        for column in cafe.__table__.columns:
            cafe_dict[column.name] = getattr(cafe, column.name)
        cafes_list.append(cafe_dict)

    return jsonify(cafes=cafes_list)


@app.route("/search", methods=["GET"])
def search():
    location = request.args.get("loc")
    cafes = db.session.execute(db.select(Cafe).where(
        Cafe.location == location)).scalars().all()
    if len(cafes) == 0:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"})
    else:
        cafes_list = []
        for cafe in cafes:
            cafe_dict = {}
            for column in cafe.__table__.columns:
                cafe_dict[column.name] = getattr(cafe, column.name)
            cafes_list.append(cafe_dict)
        return jsonify(cafes=cafes_list)

# HTTP POST - Create Record


@app.route("/add", methods=["POST"])
def add():
    data = request.form.to_dict()
    cafe = Cafe(name=data['name'],
                map_url=data['map_url'],
                img_url=data['img_url'],
                location=data['location'],
                seats=data['seats'],
                has_toilet=eval(data['has_toilet']),
                has_wifi=eval(data['has_wifi']),
                has_sockets=eval(data['has_sockets']),
                can_take_calls=eval(data['can_take_calls']),
                coffee_price=data['coffee_price'])
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    try:
        cafe = db.session.execute(db.select(Cafe).where(
            Cafe.id == cafe_id)).scalars().all()[0]
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(success="Successfully updated the price"), 200
    except IndexError:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404

# HTTP DELETE - Delete Record


@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def closed(cafe_id):
    api_key = request.args.get('api_key')
    if api_key == API_KEY:
        try:
            cafe = db.session.execute(db.select(Cafe).where(
                Cafe.id == cafe_id)).scalars().all()[0]
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(success="Successfully deleted the cafe"), 200
        except IndexError:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404
    else:
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key"), 403


if __name__ == '__main__':
    app.run(debug=True)
