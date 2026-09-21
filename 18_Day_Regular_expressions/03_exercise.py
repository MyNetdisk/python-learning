# 清理以下文本。在清理过程后，计算最常见的三个单词是什么。
paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''
import re
from collections import Counter

# 清理文本：转小写
paragraph = paragraph.lower()
# 替换非单词字符（标点符号等）为空格
paragraph = re.sub(r'\W+', ' ', paragraph)
# 按空白分割成单词列表
words = paragraph.split()
# 统计词频，取最常见的3个
word_counts = Counter(words)
top3 = word_counts.most_common(3)
print(top3)
# 输出:


# 下面的文本包含了几个电子邮件地址。编写一个可以查找或提取电子邮件地址的模式。
email_address = '''
asabeneh@gmail.com
alex@yahoo.com
kofi@yahoo.com
doe@arc.gov
asabeneh.com
asabeneh@gmail
alex@yahoo
'''
# 修复：[A-Z|a-z] → [A-Za-z]，方括号内 | 是字面字符，不是"或"
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
emails = re.findall(email_pattern, email_address)
print(emails)
# 输出: ['asabeneh@gmail.com', 'alex@yahoo.com', 'kofi@yahoo.com', 'doe@arc.gov']
