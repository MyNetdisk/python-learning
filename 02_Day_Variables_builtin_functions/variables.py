first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JavaScript', 'React', 'Python']
person_info = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki',
}

print('Hello， World') # The text Hello, World is an augument
print('Hello', ',', 'World', '!') # it can take multiple augments, for example, the comma is an augument
print(len('Hello, World!')) # The len() function returns the number of characters in a string

# 打印变量的值
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Is married:', is_married)
print('Skills:', skills)
print('Person info:', person_info)

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Finland', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)
print('Is married:', is_married)

first_name = input('What is your first name? ')
age = input('What is your age? ')

print(first_name)
print(age)

# python 中不同的数据类型
# 声明一些有各种各样数据类型的变量

first_name = 'Asabeneh' # str
last_name = 'Yetayeh' # str
country = 'Finland' # str
city = 'Helsinki' # str
age = 250 # int

# 打印变量的类型
print(type(first_name)) # <class 'str'>
print(type(last_name)) # <class 'str'>
print(type(country)) # <class 'str'>
print(type(city)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(10)) # <class 'int'>
print(type(9.81)) # <class 'float'>
print(type(1+1j)) # <class 'complex'>
print(type(True)) # <class 'bool'>
print(type([1,2,3,4])) # <class 'list'>
print(type({'name':'Asabeneh','age':250})) # <class 'dict'>
print(type((1,2,3,4))) # <class 'tuple'>
print(type({1,2,3,4})) # <class 'set'>
print(type(None)) # <class 'NoneType'>
print(type(zip([1,2,3],[4,5,6]))) # <class 'zip'>


# 整型 到 浮点型
num_int = 10
print('num_int:',num_int) # 输出 num_int: 10
num_float = float(num_int)
print('num_float:',num_float) # 输出 num_float: 10.0

# 浮点型 到 整型
gravity = 9.81
print('gravity:',gravity) # 输出 gravity: 9.81
num_int = int(gravity)
print('num_int:',num_int) # 输出 num_int: 9

# 整型 到 字符串
num_int = 10
print('num_int:',num_int) # 输出 num_int: 10
num_str = str(num_int)
print('num_str:',num_str) # 输出 num_str: '10'

# 字符串 到 整型
num_str = '10'
print('num_str:',num_str) # 输出 num_str: '10'
num_int = int(num_str)
print('num_int:',num_int) # 输出 num_int: 10

# 字符串 到 浮点型
num_str = '9.81'
print('num_str:',num_str) # 输出 num_str: '9.81'
num_float = float(num_str)
print('num_float:',num_float) # 输出 num_float: 9.81

# 浮点型 到 字符串
num_float = 9.81
print('num_float:',num_float) # 输出 num_float: 9.81
num_str = str(num_float)
print('num_str:',num_str) # 输出 num_str: '9.81'

# 字符串 到 列表
first_name = 'Asabeneh'
print('first_name:',first_name) # 输出 first_name: Asabeneh
first_name_list = list(first_name)
print('first_name_list:',first_name_list) # 输出 first_name_list: ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']