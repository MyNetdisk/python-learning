# 1、声明一个空列表
empty_list = []
print(type(empty_list))

# 2、声明一个包含 5 个以上项的列表
list_more_5 = [0, 1, 2, 3, 4, 5]
print(list_more_5)

# 3、查找列表的长度
print(len(list_more_5))

# 4、获取列表的第一项、中间项和最后一项
first_item = list_more_5[0]
middle_item = list_more_5[len(list_more_5) // 2]
last_item = list_more_5[-1]
print(first_item, middle_item, last_item)

# 5、声明一个名为 mixed_data_types 的列表
mixed_data_types = ["Qwen", 32, 168.78, False, "China"]
print(mixed_data_types)

# 6、声明 it_companies 列表
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7、使用 print() 打印列表
print(it_companies)

# 8、打印列表中的公司数
print(len(it_companies))

# 9、打印第一、中间和最后一家公司
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

# 10、修改其中一家公司的名称后打印列表
it_companies[1] = "Twitter"
print(it_companies)

# 11、向 it_companies 添加一家 IT 公司
it_companies.append("Tesla")
print(it_companies)

# 12、在公司列表中间插入一家 IT 公司
it_companies.insert(len(it_companies) // 2, "Intel")
print(it_companies)

# 13、将其中一家公司名称更改为大写（不包括 IBM!）
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14、使用字符串 '#;  ' 连接 it_companies
joined = '#;  '.join(it_companies)
print(joined)

# 15、检查 it_companies 列表中是否存在某个公司
company_to_check = "Facebook"
print(company_to_check in it_companies)

# 16、使用 sort() 方法对列表进行排序
it_companies.sort()
print(it_companies)

# 17、使用 reverse() 方法按降序反转列表
it_companies.reverse()
print(it_companies)

# 18、从列表中切分出前 3 家公司
print(it_companies[:3])

# 19、从列表中切分出最后 3 家公司
print(it_companies[-3:])

# 20、从列表中切分出中间的 IT 公司
mid = len(it_companies) // 2
print(it_companies[mid])

# 21、从列表中删除第一家 IT 公司
del it_companies[0]
print(it_companies)

# 22、从列表中删除中间的 IT 公司
del it_companies[len(it_companies) // 2]
print(it_companies)

# 23、从列表中删除最后一家 IT 公司
del it_companies[-1]
print(it_companies)

# 24、从列表中删除所有 IT 公司
it_companies.clear()
print(it_companies)

# 25、销毁 it_companies 列表
del it_companies

# 26、连接以下列表
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# 27、在连接的列表中插入 Python 和 SQL
full_stack.insert(len(full_stack), 'Python')
full_stack.insert(len(full_stack), 'SQL')
print(full_stack)
