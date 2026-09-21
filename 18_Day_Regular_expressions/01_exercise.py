# 什么是正则表达式？
# 正则表达式（Regular Expression，简称 regex）是一种用于匹配字符串中字符组合的模式，
# 常用于搜索、替换、验证和提取文本。

# 正则表达式的变量是什么？
# 指的是正则表达式中的元字符/特殊符号，如 \d（数字）、\w（单词字符）、\s（空白）、
# * + ? {n}（量词）、^ $ \b（边界）、()（分组）、|（或）等。

# 重新创建字符串模式，这些模式可以： a) 查找对带有才能的字符串的引用，在一本书中 b) 找出日期格式为 DD-MM-YYYY，例如12-01-2021 c) 找出文本中动词的时态为ing
import re

text = 'Python is an interpreted, high-level and general-purpose programming language. Python\'s design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.'

# a) 查找带引号的字符串（用捕获组提取引号内的内容）
quoted_text = 'She said "hello world" and he replied "goodbye".'
print(re.findall(r'"([^"]*)"', quoted_text))
# 输出: ['hello world', 'goodbye']

# b) 找出日期格式为 DD-MM-YYYY
date_text = "The event is on 12-01-2021 and another on 25-12-2023."
print(re.findall(r"\b\d{2}-\d{2}-\d{4}\b", date_text))
# 输出: ['12-01-2021', '25-12-2023']

# c) 找出文本中动词的时态为 ing
print(re.findall(r"\b\w+ing\b", text))
# 输出: ['interpreted', 'programming', 'emphasizes', 'using', ...] 中所有以 ing 结尾的单词
