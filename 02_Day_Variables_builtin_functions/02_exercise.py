import math

# 1. 使用 type() 检查数据类型
num_float = 23.456
print(type(num_float))  # <class 'float'>

is_married = True
print(type(is_married))  # <class 'bool'>

name_string = "John"
print(type(name_string))  # <class 'str'>

# 2. 使用 len() 计算 first name 的长度
length_str = len(name_string)
print(f"'{name_string}' 的长度是: {length_str}")  # 4
print(type(length_str))  # <class 'int'>

# 3. 比较 first name 和 last name 的长度
first_name = "John"
last_name = "Doe"
is_longer = len(first_name) > len(last_name)
print(f"'{first_name}' 比 '{last_name}' 长吗？ {is_longer}")  # True

# 4. 数学运算
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two  # 修正拼写：remainder
exp = num_one ** num_two
floor_division = num_one // num_two  # 修正拼写：floor_division

print(f"总和: {total}, 差: {diff}, 积: {product}, 商: {division}")
print(f"余数: {remainder}, 幂: {exp}, 整除: {floor_division}")

# 5. 圆的计算（半径 = 30）
radius = 30
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius  # 修正变量名：circum_of_circle

print(f"半径为 {radius} 的圆，面积是: {area_of_circle:.2f}")
print(f"半径为 {radius} 的圆，周长是: {circum_of_circle:.2f}")


# 6. 封装函数并获取用户输入
def calc_area_of_circle(r):
    return math.pi * r ** 2


def calc_circum_of_circle(r):  # 修正函数名：circum
    return 2 * math.pi * r


user_radius = int(input("请输入圆的半径: "))
print(f"用户输入半径的圆，面积是: {calc_area_of_circle(user_radius):.2f}")
print(f"用户输入半径的圆，周长是: {calc_circum_of_circle(user_radius):.2f}")  # 修正提示语

# 7. 获取用户个人信息
first_name = input("请输入您的名字 (First Name): ")  # 修正提示语
last_name = input("请输入您的姓氏 (Last Name): ")  # 修正提示语
country = input("请输入您的国家: ")
age = int(input("请输入您的年龄: "))

print(f"您好, {first_name} {last_name}! 您来自 {country}, 今年 {age} 岁。")
