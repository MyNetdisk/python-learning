# 编写一个模式，用于识别表示有效Python变量名的字符串
import re
import keyword


def is_valid_variable_name(name):
    """判断一个字符串是否是有效的Python变量名"""
    # 基础格式校验：首字符为字母或下划线，后续字符为字母、数字或下划线
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    if not re.match(pattern, name):
        return False
    # 排除Python关键字（如 class, def, return 等）
    if keyword.iskeyword(name):
        return False
    return True


# 测试
test_names = ['my_variable', '_private', 'var123', '2bad', 'class', 'user-name', 'hello world']
for name in test_names:
    result = is_valid_variable_name(name)
    print(f"'{name}' → {'合法' if result else '非法'}")

# 输出:
# 'my_variable' → 合法
# '_private' → 合法
# 'var123' → 合法
# '2bad' → 非法（数字开头）
# 'class' → 非法（关键字）
# 'user-name' → 非法（含横杠）
# 'hello world' → 非法（含空格）


# 从以下文本中清除HTML标签。
text = '''
HTML
Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.

Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.

HTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects such as interactive forms may be embedded into the rendered page. HTML provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets. Tags such as <img /> and <input /> directly introduce content into the page. Other tags such as <p> surround and provide information about document text and may include other tags as sub-elements. Browsers do not display the HTML tags, but use them to interpret the content of the page.

HTML can embed programs written in a scripting language such as JavaScript, which affects the behavior and content of web pages. Inclusion of CSS defines the look and layout of content. The World Wide Web Consortium (W3C), former maintainer of the HTML and current maintainer of the CSS standards, has encouraged the use of CSS over explicit presentational HTML since 1997.
'''

# 方法一：正则表达式（适合简单场景）
pattern = r'<.*?>'
cleaned_text = re.sub(pattern, '', text)
print(cleaned_text)

# 方法二：BeautifulSoup（推荐，能处理复杂/不规范的HTML）
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(text, 'html.parser')
# print(soup.get_text())
