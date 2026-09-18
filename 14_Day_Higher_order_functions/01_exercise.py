# 解释 map、filter 和 reduce 的区别。
# map: 它接受一个函数和可迭代对象，逐个遍历可迭代对象中的每个元素，对每个元素执行函数操作，并返回一个操作后的可迭代对象。
# filter: 它接受一个函数和可迭代对象，逐个遍历可迭代对象中的每个元素，对每个元素执行函数操作，并返回一个过滤后的可迭代对象。
# reduce: 它接受一个函数和可迭代对象，逐个遍历可迭代对象中的每个元素，对每个元素执行函数操作，并返回一个累积结果。

# 解释高阶函数、闭包和装饰器的区别。
# 高阶函数：它接受一个函数作为参数或者返回一个函数。
# 闭包：在一个函数中定义并返回一个内部函数，内部函数引用了外部函数的局部变量，即使外部函数已返回，该变量依然存活。
# 装饰器：它接受一个函数作为参数，并返回这个函数的增强版本。本质上是一个接收函数、返回函数的高阶函数。

# 定义调用函数，见示例。
def demo():
    print("Hello World")


# 方式一：直接调用
demo()

# 方式二：将函数赋值给变量，再通过变量调用
greet = demo
greet()


# 方式三：将函数作为参数传递给另一个函数
def call_func(func):
    func()


call_func(demo)

# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 使用 for 循环打印 countries 列表中的每个国家。
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)

# 使用 for 循环打印 names 列表中的每个名称。
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)

# 使用 for 循环打印 numbers 列表中的每个数字。
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)
