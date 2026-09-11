import math


# 1、声明一个名为 evens_and_odds 的函数。它接受一个正整数作为参数并计算该数内偶数和奇数的数量。
#     print(evens_and_odds(100))
#     # 偶数的数量是 51。
#     # 奇数的数量是 50。
def evens_and_odds(n):
    even = 0
    odd = 0
    for i in range(0, n + 1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return f"偶数的数量是 {even}。\n奇数的数量是 {odd}。"


print(evens_and_odds(100))


# 2、调用你的函数 factorial，它接受一个整数作为参数并返回该数的阶乘。
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


# 3、调用你的函数 is_empty，它接受一个参数并检查它是否为空。
def is_empty(param):
    if not param:
        return "The parameter is empty"
    else:
        return "The parameter is not empty"


print(is_empty(""))
print(is_empty("hello"))
print(is_empty([]))
print(is_empty(None))


# 4、编写不同的函数，它们接受列表。它们应该计算平均值、计算中位数、计算众数、计算范围、计算方差、计算标准差。

# 计算平均值
def calculate_average(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)


# 计算中位数
def calculate_median(lst):
    if len(lst) == 0:
        return 0
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        return sorted_lst[n // 2]


# 计算众数
def calculate_mode(lst):
    if len(lst) == 0:
        return 0
    # 用字典统计每个元素出现的次数
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    # 找出出现次数最多的元素
    mode = max(count_dict, key=count_dict.get)
    return mode


# 计算范围
def calculate_range(lst):
    if len(lst) == 0:
        return 0
    return max(lst) - min(lst)


# 计算方差
def calculate_variance(lst):
    if len(lst) == 0:
        return 0
    mean = calculate_average(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance


# 计算标准差
def calculate_standard_deviation(lst):
    if len(lst) == 0:
        return 0
    variance = calculate_variance(lst)
    return variance ** 0.5


# 测试统计函数
numbers = [4, 5, 6, 7, 6, 4]
print(f"平均值: {calculate_average(numbers)}")
print(f"中位数: {calculate_median(numbers)}")
print(f"众数: {calculate_mode(numbers)}")
print(f"范围: {calculate_range(numbers)}")
print(f"方差: {calculate_variance(numbers)}")
print(f"标准差: {calculate_standard_deviation(numbers)}")
