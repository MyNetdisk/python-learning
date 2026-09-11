import math


# 1、声明一个函数 add_two_numbers。它接受两个参数并返回它们的和。
def add_two_numbers(x, y):
    return x + y


print(add_two_numbers(1, 2))


# 2、圆的面积计算公式为：area = π x r x r。编写一个函数计算 area_of_circle。
def area_of_circle(r):
    return math.pi * r ** 2


print(area_of_circle(5))


# 3、编写一个名为 add_all_nums 的函数，它接受不定数量的参数并求和所有参数。检查所有列表项是否都是数字类型。如果不是，给予合理的反馈。
def add_all_nums(*args):
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            return "Error: All arguments must be numbers"
        total += num
    return total


print(add_all_nums(1, 2, 3, 4, 5))


# 4、摄氏温度（°C）可以使用以下公式转换为华氏温度（°F）：°F = (°C x 9/5) + 32。编写一个函数将 °C 转换为 °F，convert_celsius_to_fahrenheit。
def convert_celsius_to_fahrenheit(temp):
    return f'{(temp * (9 / 5) + 32):.2f}°F'


print(convert_celsius_to_fahrenheit(26))


# 5、编写一个名为 check-season 的函数，它接受一个月份作为参数并返回季节：秋季、冬季、春季或夏季。
def check_season(month):
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['January', 'February', 'December']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Unknown'


print(check_season('September'))


# 6、编写一个名为 calculate_slope 的函数，它返回线性方程的斜率。
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Error: 斜率不存在（两点在同一垂直线上）"
    return (y2 - y1) / (x2 - x1)


print(calculate_slope(1, 2, 3, 4))


# 7、二次方程按以下公式计算：ax² + bx + c = 0。编写一个函数计算二次方程的解集，solve_quadratic_eqn。
def solve_quadratic_eqn(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        return "该方程无实数根"


print(solve_quadratic_eqn(1, 2, 3))


# 8、声明一个名为 print_list 的函数。它接受一个列表作为参数，并打印列表的每个元素。
def print_list(lst):
    for item in lst:
        print(item)


print_list([1, 2, 3, 4, 5])


# 9、声明一个名为 reverse_list 的函数。它接受一个数组作为参数，并返回数组的反转（使用循环）。
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst


print(reverse_list([1, 2, 3, 4, 5]))


# 10、声明一个名为 capitalize_list_items 的函数。它接受一个列表作为参数，并返回一个大写的列表项。
def capitalize_list_items(lst):
    capitalized_lst = []
    for item in lst:
        capitalized_lst.append(item.upper())
    return capitalized_lst


print(capitalize_list_items(['potato', 'tomato', 'mango', 'milk']))


# 11、声明一个名为 add_item 的函数。它接受一个列表和一个项作为参数。它返回在末尾添加项的列表。
def add_item(lst, item):
    new_lst = lst.copy()
    new_lst.append(item)
    return new_lst


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))


# 12、声明一个名为 remove_item 的函数。它接受一个列表和一个项作为参数。它返回移除该项后的列表。
def remove_item(lst, item):
    new_lst = lst.copy()
    new_lst.remove(item)
    return new_lst


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))


# 13、声明一个名为 sum_of_numbers 的函数。它接受一个数字参数并将范围内的所有数字相加。
def sum_of_numbers(num):
    total = 0
    for i in range(num + 1):
        total += i
    return total


print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050


# 14、声明一个名为 sum_of_odds 的函数。它接受一个数字参数并将范围内的所有奇数相加。
def sum_of_odds(num):
    total = 0
    for i in range(1, num + 1, 2):
        total += i
    return total


print(sum_of_odds(5))


# 15、声明一个名为 sum_of_even 的函数。它接受一个数字参数并将范围内的所有偶数相加。
def sum_of_evens(num):
    total = 0
    for i in range(0, num + 1, 2):
        total += i
    return total


print(sum_of_evens(5))
