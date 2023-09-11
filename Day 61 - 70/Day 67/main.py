from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)

# CKEDITOR
ckeditor = CKEditor(app)


# NEW POST FORM
class NewPost(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    blog_content = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField("SUBMIT POST")


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/', methods=['GET'])
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts
@app.route('/post/<post_id>', methods=["GET"])
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new():
    form = NewPost()
    current_date = date.today().strftime("%B %d, %Y")
    print(current_date)
    if form.validate_on_submit():
        response = request.form.to_dict()
        new_blog = BlogPost(title=response['title'], subtitle=response['subtitle'], date=current_date,
                            body=response['blog_content'], author=response['author'], img_url=response['img_url'])
        db.session.add(new_blog)
        db.session.commit()
        return redirect("/")
    return render_template("make-post.html", title="New Post", form=form)


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<post_id>", methods=['GET', 'POST'])
def edit(post_id):
    post = db.get_or_404(BlogPost, post_id)
    form = NewPost(title=post.title,
                   subtitle=post.subtitle,
                   author=post.author,
                   img_url=post.img_url,
                   blog_content=post.body)
    if form.validate_on_submit():
        response = request.form.to_dict()
        post.title = response['title']
        post.subtitle = response['subtitle']
        post.body = response['blog_content']
        post.author = response['author']
        post.img_url = response['img_url']
        db.session.commit()
        return redirect(f"/post/{post_id}")
    return render_template("make-post.html", form=form, title="Edit Post")


# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<post_id>')
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect("/")


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
