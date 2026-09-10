# 1、使用 for 循环从 0 到 100 遍历并输出所有数字的和
total = 0
for i in range(101):
    total += i
print(f"The sum of all numbers is {total}.")

# 2、使用 for 循环从 0 到 100 遍历并分别输出奇数和偶数的和
odd_total = 0
even_total = 0
for i in range(101):
    if i % 2 == 0:
        even_total += i
    else:
        odd_total += i
print(f"The sum of all odd numbers is {odd_total}. And the sum of all even numbers is {even_total}.")
