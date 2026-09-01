# ========== 第1-10题 ==========

# 1. 将字符串 'Thirty', 'Days', 'Of', 'Python' 连接为一个字符串
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
result1 = str1 + ' ' + str2 + ' ' + str3 + ' ' + str4
result2 = ' '.join([str1, str2, str3, str4])
result3 = f'{str1} {str2} {str3} {str4}'

print(result1)  # 输出: Thirty Days Of Python
print(result2)  # 输出: Thirty Days Of Python
print(result3)  # 输出: Thirty Days Of Python

# 2. 将字符串 'Coding', 'For', 'All' 连接为一个字符串
words_coding = ['Coding', 'For', 'All']
result1 = words_coding[0] + ' ' + words_coding[1] + ' ' + words_coding[2]
result2 = ' '.join(words_coding)
result3 = f'{words_coding[0]} {words_coding[1]} {words_coding[2]}'

print(result1)  # 输出: Coding For All
print(result2)  # 输出: Coding For All
print(result3)  # 输出: Coding For All

# 3. 声明一个名为 company 的变量，并赋值为 "Coding For All"
company = "Coding For All"

# 4. 使用 print() 打印变量 company
print(company)  # 输出: Coding For All

# 5. 使用 len() 和 print() 打印 company 字符串的长度
print(len(company))  # 输出: 14

# 6. 使用 upper() 方法将所有字符更改为大写字母
print(company.upper())  # 输出: CODING FOR ALL

# 7. 使用 lower() 方法将所有字符更改为小写字母
print(company.lower())  # 输出: coding for all

# 8. 使用 capitalize()、title() 和 swapcase() 方法格式化字符串
print(company.capitalize())  # 输出: Coding for all
print(company.title())  # 输出: Coding For All
print(company.swapcase())  # 输出: cODING fOR aLL

# 9. 切片出 Coding For All 字符串的第一个单词
print(company.split()[0])  # 输出: Coding

# 10. 检查 Coding For All 字符串是否包含单词 Coding
print('Coding' in company)  # 输出: True（最 Pythonic 的方式）
print(company.find('Coding') != -1)  # 输出: True

# ========== 第11-20题 ==========

# 11. 将字符串 'Coding For All' 中的单词 Coding 替换为 Python
print(company.replace('Coding', 'Python'))  # 输出: Python For All

# 12. 将 Python for Everyone 替换为 Python for All
pfe = "Python for Everyone"
print(pfe.replace('Everyone', 'All'))  # 输出: Python for All

# 13. 使用空格作为分隔符拆分字符串 'Coding For All'
print(company.split())  # 输出: ['Coding', 'For', 'All']

# 14. 在逗号处拆分字符串
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(','))

# 15. 字符串 Coding For All 中索引 0 处的字符是什么
print(company[0])  # 输出: C

# 16. 字符串 Coding For All 的最后一个索引是什么
print(len(company) - 1)  # 输出: 13

# 17. 字符串 Coding For All 中索引 10 处的字符是什么
print(company[10])  # 输出: A

# 18. 为字符串 'Python For Everyone' 创建首字母缩略词
pfe = "Python For Everyone"
acro_pfe = ''.join(word[0] for word in pfe.split())
print(acro_pfe)  # 输出: PFE

# 19. 为名称 'Coding For All' 创建首字母缩略词
cfa = 'Coding For All'
acro_cfa = ''.join(word[0] for word in cfa.split())
print(acro_cfa)  # 输出: CFA

# 20. 使用索引确定 'Coding For All' 中 C 第一次出现的位置
print(company.index('C'))  # 输出: 0

# ========== 第21-30题 ==========

# 21. 使用索引确定 'Coding For All' 中 F 第一次出现的位置
print(company.index('F'))  # 输出: 7

# 22. 使用 rfind 确定 'Coding For All People' 中 l 最后一次出现的位置
cfap = 'Coding For All People'
print(cfap.rfind('l'))  # 输出: 18

# 23. 查找单词 'because' 第一次出现的位置
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))  # 输出: 32
print(sentence.find('because'))  # 输出: 32

# 24. 使用 rindex 查找单词 because 最后一次出现的位置
print(sentence.rindex('because'))  # 输出: 41

# 25. 删除短语 'because because because'
print(sentence.replace('because because because', ''))

# 26. 查找单词 'because' 第一次出现的位置（与第23题相同）
print(sentence.index('because'))  # 输出: 32

# 27. 删除短语 'because 因为 because'
# 注意：原句中并没有中文"因为"，题目可能存在翻译笔误
# 如果按字面意思执行，原句不会发生变化
print(sentence.replace('because 因为 because', ''))

# 28. 'Coding For All' 是否以子字符串 Coding 开头？
print(company.startswith('Coding'))  # 输出: True

# 29. 'Coding For All' 是否以子字符串 coding 结尾？
print(company.endswith('coding'))  # 输出: False

# 30. 删除给定字符串中左右空格
# 原题中的 &nbsp; 是 HTML 空格实体，这里用普通空格代替
print('   Coding For All      '.strip())  # 输出: Coding For All

# ========== 第31-36题 ==========

# 31. 使用 isidentifier() 判断哪个变量名合法
print('30DaysOfPython'.isidentifier())  # 输出: False（不能以数字开头）
print('thirty_days_of_python'.isidentifier())  # 输出: True

# 32. 使用空格连接列表中的字符串
print(' '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# 33. 使用换行转义序列分隔句子
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34. 使用制表符转义序列输出表格（使用 f-string 精确对齐）
print(f"{'Name':<10}{'Age':<8}{'Country':<10}{'City'}")
print(f"{'Asabeneh':<10}{'250':<8}{'Finland':<10}{'Helsinki'}")

# 35. 使用字符串格式化方法输出圆面积计算
radius = 10
area = 3.14 * radius ** 2
print(f'radius = {radius}')
print(f'area = 3.14 * radius ** 2')
print(f'The area of a circle with radius {radius} is {int(area)} meters square.')

# 36. 使用字符串格式化方法输出算术运算结果
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
