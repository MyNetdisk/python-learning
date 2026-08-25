import math

# 1. 年龄：整型
age = 32

# 2. 身高：浮点型
body_height = 168.78

# 3. 复数变量
complex_number = 1 + 2j

print("age:", age, type(age))
print("body_height:", body_height, type(body_height))
print("complex_number:", complex_number, type(complex_number))


# 4. 三角形面积
def calc_triangle_area():
    """计算三角形面积：0.5 * 底 * 高"""
    b = float(input("请输入三角形的底: "))
    h = float(input("请输入三角形的高: "))
    area = 0.5 * b * h
    print(f"三角形的面积是 {area:g}")
    return area


# calc_triangle_area()


# 5. 三角形周长
def calc_triangle_perimeter():
    """计算三角形周长：a + b + c"""
    a = float(input("请输入三角形的边 a: "))
    b = float(input("请输入三角形的边 b: "))
    c = float(input("请输入三角形的边 c: "))
    perimeter = a + b + c
    print(f"三角形的周长是 {perimeter:g}")
    return perimeter


# calc_triangle_perimeter()


# 6. 矩形面积和周长
def calc_rectangle():
    """计算矩形面积和周长"""
    length = float(input("请输入矩形的长度: "))
    width = float(input("请输入矩形的宽度: "))

    area = length * width
    perimeter = 2 * (length + width)

    print(f"矩形面积是 {area:g}")
    print(f"矩形周长是 {perimeter:g}")
    return area, perimeter


# calc_rectangle()


# 7. 圆的面积和周长
def calc_circle():
    """计算圆的面积和周长，pi = 3.14"""
    pi = 3.14
    r = float(input("请输入圆的半径: "))

    area = pi * r * r
    circumference = 2 * pi * r

    print(f"圆的面积是 {area:g}")
    print(f"圆的周长是 {circumference:g}")
    return area, circumference


# calc_circle()


# 8. y = 2x - 2 的斜率、x 截距、y 截距
slope = 2
y_intercept = -2
x_intercept = 1.0  # 2x - 2 = 0 时，x = 1

print(f"y = 2x - 2 的斜率是 {slope}")
print(f"y 截距是 {y_intercept}")
print(f"x 截距是 {x_intercept}")

# 9. 两点之间的斜率和欧几里得距离
x1, y1 = 2, 2
x2, y2 = 6, 10

slope_from_points = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"两点 (2,2) 和 (6,10) 的斜率是 {slope_from_points}")
print(f"两点之间的欧几里得距离是 {distance:.2f}")

# 10. 比较练习 8 和练习 9 的斜率
print(f"两个斜率是否相等？ {slope == slope_from_points}")


# 11. y = x^2 + 6x + 9，找出 y 何时为 0
def calculate_y(x):
    """计算 y = x^2 + 6x + 9"""
    return x ** 2 + 6 * x + 9


x_values = [-5, -4, -3, -2, -1, 0, 1, 2]

print("x\ty")
print("-" * 10)
for x in x_values:
    print(f"{x}\t{calculate_y(x)}")

print("\n寻找 y = 0 的 x 值：")
for x in range(-20, 21):
    if calculate_y(x) == 0:
        print(f"当 x = {x} 时，y = 0")

# 12. 'python' 和 'dragon' 的长度，并写一个假比较
length_python = len("python")
length_dragon = len("dragon")

print(f"'python' 的长度是 {length_python}")
print(f"'dragon' 的长度是 {length_dragon}")
print(f"长度是否相等？ {length_python == length_dragon}")  # False

# 13. 检查 'python' 和 'dragon' 中是否都有 'on'
has_on_in_python = "on" in "python"
has_on_in_dragon = "on" in "dragon"

print(f"'python' 和 'dragon' 中是否都有 'on': {has_on_in_python and has_on_in_dragon}")

# 14. 检查句子中是否有 jargon
sentence = "I hope this course is not full of jargon"
print(f"句子中是否包含 'jargon': {'jargon' in sentence}")

# 15. 'dragon' 和 'python' 中都没有 'on'
print(f"'dragon' 和 'python' 中都没有 'on': {'on' not in 'dragon' and 'on' not in 'python'}")

# 16. 把 'python' 的长度转成浮点数，再转成字符串
length_python = len("python")
length_as_float = float(length_python)
length_as_string = str(length_as_float)

print(f"'python' 的长度: {length_python}")
print(f"转换为浮点数: {length_as_float}")
print(f"再转换为字符串: {length_as_string}")


# 17. 检查一个数字是偶数还是奇数
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} 是偶数")
    else:
        print(f"{number} 是奇数")


check_even_odd(5)
check_even_odd(6)

# 18. 检查 7 // 3 是否等于 int(2.7)
print(f"7 // 3 == int(2.7): {7 // 3 == int(2.7)}")

# 19. 检查 '10' 的类型是否等于 10 的类型
print(f"type('10') == type(10): {type('10') == type(10)}")

# 20. 检查 int('9.8') 是否等于 10
try:
    result = int('9.8') == 10
except ValueError:
    result = False

print(f"int('9.8') == 10: {result}")


# 21. 工资计算
def calculate_salary():
    hours = int(input("请输入工时: "))
    rate = int(input("请输入时薪: "))
    salary = hours * rate
    print(f"你每周的薪资是 {salary}")
    return salary


# calculate_salary()


# 22. 计算一个人活了多少秒
def calculate_seconds_lived():
    years = int(input("请输入你已经活了多少年: "))
    seconds_lived = years * 365 * 24 * 60 * 60
    print(f"你已经活了 {seconds_lived} 秒.")
    return seconds_lived


# calculate_seconds_lived()


# 23. 显示表格
def square(x):
    return x ** 2


def cube(x):
    return x ** 3


print("n  1  n  n^2  n^3")
for i in range(1, 6):
    print(i, 1, i, square(i), cube(i))
