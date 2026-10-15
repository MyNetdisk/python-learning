from flask import Flask
from extensions import db
from blueprints.grade import grade_bp
from blueprints.bmi import bmi_bp
from blueprints.blog import blog_bp
from blueprints.todo import todo_bp

app = Flask(__name__)
app.secret_key = "dev-secret"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(grade_bp, url_prefix="/grade")
app.register_blueprint(bmi_bp, url_prefix="/bmi")
app.register_blueprint(blog_bp, url_prefix="/blog")
app.register_blueprint(todo_bp, url_prefix="/todo")


@app.route("/")
def index():
    return """
    <h1>Flask 多模块练习项目</h1>
    <ul>
        <li><a href="/grade">成绩计算器</a></li>
        <li><a href="/bmi">BMI 计算器</a></li>
        <li><a href="/blog">博客应用</a></li>
        <li><a href="/todo">任务管理器</a></li>
    </ul>
    """


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
