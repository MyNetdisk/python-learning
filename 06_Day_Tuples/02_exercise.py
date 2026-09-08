# 1、从 family_members 中获取兄弟姐妹和父母
family_members = ('sister1', 'sister2', 'brother1', 'brother2', 'mother', 'father')
siblings = family_members[:4]
parents = family_members[4:]
print(f"兄弟姐妹: {siblings}")
print(f"父母: {parents}")

# 2、创建 fruits、vegetables 和 animal products 元组，连接并分配给 food_stuff_tp
fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'meat', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products
print(f"食物元组: {food_stuff_tp}")

# 3、将 food_stuff_tp 元组更改为 food_stuff_lt 列表
food_stuff_lt = list(food_stuff_tp)
print(f"食物列表: {food_stuff_lt}")

# 4、从 food_stuff_tp 元组中切出中间项或项
n = len(food_stuff_tp)
if n % 2 == 0:
    middle_items = food_stuff_tp[n // 2 - 1: n // 2 + 1]
    print(f"中间项（偶数个）: {middle_items}")
else:
    middle_item = food_stuff_tp[n // 2]
    print(f"中间项（奇数个）: {middle_item}")

# 5、从 food_stuff_lt 列表中切出前三项和最后三项
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print(f"前三项: {first_three_items}")
print(f"最后三项: {last_three_items}")

# 6、完全删除 food_stuff_tp 元组
del food_stuff_tp
print("food_stuff_tp 已被删除")

# 7、检查元组中是否存在项
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# 检查 'Estonia' 是否在 nordic_countries 元组中
print(f"'Estonia' 是否在 nordic_countries 中: {'Estonia' in nordic_countries}")

# 检查 'Iceland' 是否在 nordic_countries 元组中
print(f"'Iceland' 是否在 nordic_countries 中: {'Iceland' in nordic_countries}")
