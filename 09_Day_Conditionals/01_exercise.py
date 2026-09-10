# 1、使用 input 获取用户输入，判断是否可以学习驾驶
age = int(input("输入你的年龄："))
if age >= 18:
    print("你已经足够大，可以学习驾驶。")
else:
    print(f"你还需要等待{18 - age}年才能学习驾驶。")

# 2、使用 if…else 比较 my_age 和 your_age 的值
my_age = 18
your_age = int(input("输入你的年龄："))
if my_age > your_age:
    diff = my_age - your_age
    print(f"我比你大{diff}年。")
elif my_age < your_age:
    diff = your_age - my_age
    print(f"你比我大{diff}年。")
else:
    print("我们一样大。")

# 3、使用输入提示从用户处获得两个数字，比较大小
a = int(input("输入第一个数字："))
b = int(input("输入第二个数字："))
if a > b:
    print(f"{a}大于{b}")
elif a < b:
    print(f"{a}小于{b}")
else:
    print(f"{a}等于{b}")
