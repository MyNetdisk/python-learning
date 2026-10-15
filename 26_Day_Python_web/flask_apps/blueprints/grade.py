from flask import Blueprint, render_template, request

grade_bp = Blueprint("grade", __name__)


@grade_bp.route("/", methods=["GET", "POST"])
def calculator():
    message = None
    subject = None
    score = None

    if request.method == "POST":
        subject = request.form.get("subject", "").strip()
        score_text = request.form.get("score", "").strip()

        if not subject:
            message = "请输入科目名称。"
        elif not score_text:
            message = "请输入分数。"
        else:
            try:
                score = float(score_text)
            except ValueError:
                message = "分数必须是数字。"
                score = None

            if score is not None:
                if score < 0 or score > 100:
                    message = "分数必须在 0 到 100 之间。"
                elif score >= 90:
                    message = f"优秀！你的{subject}成绩是{score}"
                elif score >= 80:
                    message = f"很好！你的{subject}成绩是{score}"
                elif score >= 70:
                    message = f"一般！你的{subject}成绩是{score}"
                elif score >= 60:
                    message = f"及格！你的{subject}成绩是{score}"
                else:
                    message = f"你需要更加努力！你的{subject}成绩是{score}"

    return render_template(
        "grade.html",
        message=message,
        subject=subject,
        score=score,
    )
