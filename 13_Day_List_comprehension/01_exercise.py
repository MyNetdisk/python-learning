# 使用列表推导式过滤出列表中的负数和零：
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_negative_and_zero = [number for number in numbers if number > 0]
print(filter_negative_and_zero)

# 将以下列表中的列表展平为一维列表：
# list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# 输出:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]
print(flatten_list)

# 使用列表推导式创建以下元组列表：
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# ...
# (10, 1, 10, 100, 1000, 10000, 100000)]
list_comprehension = [(i, 1, i, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(list_comprehension)

# 将以下列表展平成一个新列表：
# countries = [[('芬兰', '赫尔辛基')], [('瑞典', '斯德哥尔摩')], [('挪威', '奥斯陆')]]
# 输出:
# [['芬兰', 'FIN', '赫尔辛基'], ['瑞典', 'SWE', '斯德哥尔摩'], ['挪威', 'NOR', '奥斯陆']]
countries = [[('芬兰', '赫尔辛基')], [('瑞典', '斯德哥尔摩')], [('挪威', '奥斯陆')]]
country_codes = {'芬兰': 'FIN', '瑞典': 'SWE', '挪威': 'NOR'}
flatten_countries = [
    [country, country_codes[country], city]
    for sublist in countries
    for country, city in sublist
]
print(flatten_countries)

# 将以下列表转换为字典列表：
# countries = [[('芬兰', '赫尔辛基')], [('瑞典', '斯德哥尔摩')], [('挪威', '奥斯陆')]]
# 输出:
# [{'国家': '芬兰', '城市': '赫尔辛基'},
# {'国家': '瑞典', '城市': '斯德哥尔摩'},
# {'国家': '挪威', '城市': '奥斯陆'}]
countries = [[('芬兰', '赫尔辛基')], [('瑞典', '斯德哥尔摩')], [('挪威', '奥斯陆')]]
countries_dict = [{'国家': country[0], '城市': country[1]} for sublist in countries for country in sublist]
print(countries_dict)

# 将以下列表转换为连接字符串的列表：
# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# 输出:
# ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
flatten_names = [f"{first} {last}" for sublist in names for first, last in sublist]
print(flatten_names)

# 编写一个 lambda 函数，可以求解线性函数的斜率或 y 截距。
# 斜率 = (y2 - y1) / (x2 - x1)
# y 截距 = y1 - slope * x1
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x1, y1, x2, y2: y1 - ((y2 - y1) / (x2 - x1)) * x1

print(f"斜率: {slope(1, 2, 3, 4)}")  # 1.0
print(f"y 截距: {y_intercept(1, 2, 3, 4)}")  # 1.0
