from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db

blog_bp = Blueprint("blog", __name__)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)


@blog_bp.route("/")
def index():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template("blog/index.html", posts=posts)


@blog_bp.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        if title and content:
            post = Post(title=title, content=content)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for("blog.index"))
    return render_template("blog/add.html")


@blog_bp.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == "POST":
        post.title = request.form.get("title", "").strip()
        post.content = request.form.get("content", "").strip()
        if post.title and post.content:
            db.session.commit()
            return redirect(url_for("blog.index"))
    return render_template("blog/edit.html", post=post)


@blog_bp.route("/delete/<int:post_id>", methods=["POST"])
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("blog.index"))
