from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db

todo_bp = Blueprint("todo", __name__)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)


@todo_bp.route("/")
def index():
    tasks = Task.query.order_by(Task.id.desc()).all()
    return render_template("todo/index.html", tasks=tasks)


@todo_bp.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    if title:
        task = Task(title=title)
        db.session.add(task)
        db.session.commit()
    return redirect(url_for("todo.index"))


@todo_bp.route("/toggle/<int:task_id>", methods=["POST"])
def toggle(task_id):
    task = Task.query.get_or_404(task_id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for("todo.index"))


@todo_bp.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("todo.index"))
