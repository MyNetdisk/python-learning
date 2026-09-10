# 1、根据学生的分数给出等级
score = int(input("输入学生的分数："))
if 80 <= score <= 100:
    print("A")
elif 70 <= score < 80:
    print("B")
elif 60 <= score < 70:
    print("C")
elif 50 <= score < 60:
    print("D")
elif 0 <= score < 50:
    print("F")
else:
    print("输入的分数无效，请输入 0-100 之间的分数。")

# 2、检查是否是秋天、冬天、春天或夏天
month = int(input("输入月份："))
if month in (9, 10, 11):
    print("秋天")
elif month in (12, 1, 2):
    print("冬天")
elif month in (3, 4, 5):
    print("春天")
elif month in (6, 7, 8):
    print("夏天")
else:
    print("输入的月份不存在")

# 3、如果列表中不存在某个水果，则将其添加到列表中
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("输入水果名称：").lower()
if fruit in fruits:
    print("该水果已在列表中")
else:
    fruits.append(fruit)
    print(f"修改后的列表: {fruits}")
