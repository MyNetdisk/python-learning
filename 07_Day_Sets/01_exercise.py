# 集合
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1、找到集合 it_companies 的长度
print(f"集合长度: {len(it_companies)}")

# 2、向 it_companies 添加 'Twitter'
it_companies.add('Twitter')
print(f"添加 Twitter 后: {it_companies}")

# 3、一次性向集合 it_companies 插入多个 IT 公司
it_companies.update({'LinkedIn', 'Telegram'})
print(f"插入多个公司后: {it_companies}")

# 4、从集合 it_companies 中移除一家公司
it_companies.remove('Twitter')
print(f"移除 Twitter 后: {it_companies}")

# 5、移除和丢弃之间有什么区别
# remove()：移除不存在的元素会报错（KeyError）
# discard()：移除不存在的元素不会报错

# 演示 discard()：移除不存在的元素，不会报错
it_companies.discard('Netflix')
print(f"使用 discard 移除不存在的 'Netflix'，不会报错: {it_companies}")

# 演示 remove()：移除不存在的元素，会报错
# it_companies.remove('Netflix')  # 取消注释会报错：KeyError: 'Netflix'
print("使用 remove 移除不存在的元素会报 KeyError（已注释避免程序崩溃）")
