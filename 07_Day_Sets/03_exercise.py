# 集合
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1、将年龄转换为集合并比较列表和集合的长度，哪一个更大？
age_set = set(age)
print(f"列表长度: {len(age)}")
print(f"集合长度: {len(age_set)}")
if len(age) > len(age_set):
    print("列表长度更大（因为列表中有重复元素）")
elif len(age_set) > len(age):
    print("集合长度更大")
else:
    print("两者长度相等")

# 2、解释以下数据类型之间的区别：字符串、列表、元组和集合
# 字符串：有序的、不可变的字符序列，用引号包裹
# 列表：有序的、可变的、可重复的集合，用方括号 [] 包裹
# 元组：有序的、不可变的、可重复的集合，用圆括号 () 包裹
# 集合：无序的、可变的、不可重复的集合，用花括号 {} 包裹
# 核心区别：
#   - 有序 vs 无序：字符串、列表、元组有序；集合无序
#   - 可变 vs 不可变：列表、集合可变；字符串、元组不可变
#   - 可重复 vs 不可重复：字符串、列表、元组可重复；集合不可重复

# 3、这句句子中用了多少独特的单词？使用 split 方法和集合来获取独特的单词
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print(f"总单词数: {len(words)}")
print(f"独特单词数: {len(unique_words)}")
print(f"独特单词: {unique_words}")
