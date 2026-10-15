from flask import Blueprint, render_template, request

bmi_bp = Blueprint("bmi", __name__)


@bmi_bp.route("/", methods=["GET", "POST"])
def calculator():
    message = None
    weight = None
    height_cm = None
    bmi = None

    if request.method == "POST":
        weight_text = request.form.get("weight", "").strip()
        height_text = request.form.get("height", "").strip()

        if not weight_text:
            message = "请输入体重（kg）。"
        elif not height_text:
            message = "请输入身高（cm）。"
        else:
            try:
                weight = float(weight_text)
            except ValueError:
                message = "体重必须是数字。"

            try:
                height_cm = float(height_text)
            except ValueError:
                message = "身高必须是数字。"

            if weight is not None and height_cm is not None:
                if weight <= 0:
                    message = "体重必须大于 0。"
                elif height_cm <= 0:
                    message = "身高必须大于 0。"
                else:
                    height_m = height_cm / 100
                    bmi = weight / (height_m ** 2)
                    bmi_rounded = round(bmi, 2)

                    if bmi < 18.5:
                        status = "体重过轻"
                    elif bmi < 24.9:
                        status = "健康体重"
                    elif bmi < 29.9:
                        status = "超重"
                    else:
                        status = "肥胖"

                    message = f"你的 BMI 是 {bmi_rounded}，属于：{status}"

    return render_template(
        "bmi.html",
        message=message,
        weight=weight,
        height_cm=height_cm,
        bmi=bmi,
    )
