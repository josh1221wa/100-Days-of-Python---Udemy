from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-is-the-secret-key'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)


# LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return db.get_or_404(User, id)


# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        response = request.form.to_dict()
        hashed_password = generate_password_hash(
            password=response['password'], method="pbkdf2:sha256", salt_length=8)
        new_user = User(
            email=response['email'], password=hashed_password, name=response['name'])
        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('secrets'))
        except IntegrityError:
            flash("You've already signed up with that email, log in instead!")
            return redirect("/register")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        user = db.session.execute(
            db.select(User).where(User.email == email)).scalar()
        if user is None:
            flash("This email does not exist, please try again.")
            return redirect(url_for("login"))
        if check_password_hash(pwhash=user.password, password=request.form.get('password')):
            login_user(user)
            return redirect("/secrets")
        else:
            flash("Password incorrect, please try again.")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/download')
@login_required
def download():
    return send_from_directory("static", path="files/cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
    # with app.app_context():
    #     users = db.session.execute(db.select(User)).scalars()

    #     for user in users:
    #         db.session.delete(user)
    #         db.session.commit()
