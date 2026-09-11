import keyword
import math
from data.countries_data import countries_data


# 1、编写一个名为 is_prime 的函数，检查一个数是否是质数。
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


print(is_prime(2))  # True
print(is_prime(4))  # False
print(is_prime(17))  # True


# 2、编写一个函数检查列表中的所有项是否都是唯一的。
def are_all_items_unique(lst):
    return len(lst) == len(set(lst))


print(are_all_items_unique([1, 2, 3, 4]))  # True
print(are_all_items_unique([1, 2, 3, 3, 4]))  # False


# 3、编写一个函数检查列表中的所有项是否都是相同的数据类型。
def check_same_type(lst):
    if len(lst) == 0:
        return '列表为空'
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return '列表中的项类型不同'
    return '列表中的所有项都是相同的数据类型'


print(check_same_type([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(check_same_type([1, 2, 3, 4, 5, 6, 7, 8, '9']))


# 4、编写一个函数检查提供的变量是否是一个有效的 python 变量。
def is_valid_variable(name):
    """
    检查一个字符串是否是有效的 Python 变量名
    :param name:
    :return:
    """
    if not isinstance(name, str):
        return False
    # str.isidentifier() 检查是否是合法的标识符（字母/下划线开头，只含字母数字下划线）
    # keyword.iskeyword() 检查是否是 Python 关键字
    return name.isidentifier() and not keyword.iskeyword(name)


print(is_valid_variable('my_var'))  # True
print(is_valid_variable('123var'))  # False
print(is_valid_variable('for'))  # False
print(is_valid_variable('my-var'))  # False


# 5、访问数据文件并访问 countries-data.py 文件。

# 6、创建一个名为 most_spoken_languages 的函数。它返回世界上使用最多的 10 或 20 种语言，按降序排列。
def most_spoken_languages(n=10):
    languages = {}
    for country in countries_data:
        for language in country['languages']:
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1
    # 转成列表后用冒泡排序，按使用人数降序
    list_of_languages = list(languages.items())
    for i in range(len(list_of_languages)):
        for j in range(len(list_of_languages) - 1 - i):
            if list_of_languages[j][1] < list_of_languages[j + 1][1]:
                list_of_languages[j], list_of_languages[j + 1] = list_of_languages[j + 1], list_of_languages[j]
    return list_of_languages[:n]


print(most_spoken_languages())
print(most_spoken_languages(20))


# 7、创建一个名为 most_populated_countries 的函数。它返回世界上人口最多的 10 或 20 个国家，按降序排列。
def most_populated_countries(n=10):
    # 提取国家名和人口组成列表，用冒泡排序按人口降序
    list_of_countries = []
    for country in countries_data:
        list_of_countries.append((country['name'], country['population']))
    for i in range(len(list_of_countries)):
        for j in range(len(list_of_countries) - 1 - i):
            if list_of_countries[j][1] < list_of_countries[j + 1][1]:
                list_of_countries[j], list_of_countries[j + 1] = list_of_countries[j + 1], list_of_countries[j]
    return list_of_countries[:n]


print(most_populated_countries())
print(most_populated_countries(20))
