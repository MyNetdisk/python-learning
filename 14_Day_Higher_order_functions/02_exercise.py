from functools import reduce
# 注意：实际项目中需要从模块导入，确保 data countries_data.py 存在
from data.countries_data import countries_data

# 为了独立运行演示，这里用题目给定的短列表 + 模拟数据
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 模拟 countries_data（实际应从文件导入）
# countries_data = [
#     {'name': 'Estonia'}, {'name': 'Finland'}, {'name': 'Sweden'},
#     {'name': 'Denmark'}, {'name': 'Norway'}, {'name': 'Iceland'},
#     {'name': 'Ireland'}, {'name': 'Poland'}, {'name': 'Germany'},
#     {'name': 'Netherlands'}, {'name': 'Belgium'}, {'name': 'France'},
# ]

# 使用 map 将 countries 列表中的每个国家更改为大写，生成一个新列表。
countries_upper = list(map(lambda country: country.upper(), countries))
print(countries_upper)

# 使用 map 将 numbers 列表中的每个数字更改为平方，生成一个新列表。
numbers_square = list(map(lambda num: num ** 2, numbers))
print(numbers_square)  # numbers_square 已经是列表，无需再包 list()

# 使用 map 将 names 列表中的每个名称更改为大写，生成一个新列表。
names_upper = list(map(lambda name: name.upper(), names))
print(names_upper)

# 使用 filter 过滤出包含"land"的国家。
land_countries = list(filter(lambda country: 'land' in country.lower(), countries))
print(land_countries)

# 使用 filter 过滤出正好六个字符的国家。
six_char_countries = list(filter(lambda country: len(country) == 6, countries))
print(six_char_countries)

# 使用 filter 过滤出包含六个字母及以上的国家。
six_or_more_char_countries = list(filter(lambda country: len(country) >= 6, countries))
print(six_or_more_char_countries)

# 使用 filter 过滤出以'E'开头的国家。
e_countries = list(filter(lambda country: country.startswith('E'), countries))
print(e_countries)

# 链接两个或多个列表迭代器（例如 arr.map(callback).filter(callback).reduce(callback)）。
# 示例：先对数字求平方(map)，再过滤大于50的(filter)，最后求和(reduce)
chained_result = reduce(
    lambda x, y: x + y,
    filter(lambda x: x > 50, map(lambda x: x ** 2, numbers))
)
print(chained_result)  # 8^2=64 + 9^2=81 + 10^2=100 = 245


# 声明一个函数 get_string_lists，它接收一个列表作为参数并返回一个仅包含字符串项的列表。
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))


print(get_string_lists([1, 2, 3, 'a', 'b', 'c']))

# 使用 reduce 对 numbers 列表中的所有数字求和。
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

# 使用 reduce 将所有国家连接起来，生成句子：
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# 用切片 countries[:-1] 取除最后一个外的所有国家，reduce 用 ', ' 连接，
# 最后拼接 ', and ' + 最后一个国家 + ' are north European countries'
sentence = (
        reduce(lambda x, y: x + ', ' + y, countries[:-1])
        + ', and '
        + countries[-1]
        + ' are north European countries'
)
print(sentence)


# 声明一个函数 categorize_countries，返回一个包含某种通用模式的国家列表
# （可以在本仓库的 countries.js 文件中找到国家列表，例如 'land', 'ia', 'island', 'stan'）。
def categorize_countries(countries_data):
    patterns = ['land', 'ia', 'island', 'stan']
    return [
        country['name']
        for country in countries_data
        if any(pattern in country['name'].lower() for pattern in patterns)
    ]


# 如果有完整的 countries_data 数据，可以这样调用：
print(categorize_countries(countries_data))


# 创建一个返回字典的函数，其中键表示国家名称的首字母，值表示以该字母开头的国家数。
def count_countries_by_first_letter(countries_data):
    result = {}
    for country in countries_data:
        name = country['name'].strip()
        if name:  # 跳过空字符串
            first_letter = name[0].upper()  # 统一大写，避免 'a' 和 'A' 被分开统计
            result[first_letter] = result.get(first_letter, 0) + 1
    return result


print(count_countries_by_first_letter(countries_data))


# 声明一个 get_first_ten_countries 函数 - 它返回数据文件夹中 countries.js 列表中的前十个国家。
def get_first_ten_countries(countries_data):
    return [country['name'] for country in countries_data[:10]]


print(get_first_ten_countries(countries_data))


# 声明一个 get_last_ten_countries 函数 - 它返回国家列表中的最后十个国家。
def get_last_ten_countries(countries_data):
    return [country['name'] for country in countries_data[-10:]]


print(get_last_ten_countries(countries_data))
