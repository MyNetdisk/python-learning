# 1、分别使用 while 和 for 实现从 0 到 10 的迭代
i = 0
while i <= 10:
    print(i)
    i += 1

for i in range(11):
    print(i)

# 2、分别使用 while 和 for 实现从 10 到 0 的迭代
item = 10
while item >= 0:
    print(item)
    item -= 1

for item in range(10, -1, -1):
    print(item)

# 3、写一个循环，输出三角形
for i in range(1, 8):
    print("#" * i)

# 4、使用嵌套循环输出 8x8 的 # # # 网格
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

# 5、使用循环输出乘法表
for i in range(11):
    print(f'{i} x {i} = {i * i}')

# 6、用 for 循环遍历列表并打印每个元素
for item in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
    print(item)

# 7、用 for 循环从 0 到 100 遍历并打印所有偶数
for i in range(0, 101, 2):
    print(i)

# 8、用 for 循环从 0 到 100 遍历并打印所有奇数
for i in range(1, 101, 2):
    print(i)
