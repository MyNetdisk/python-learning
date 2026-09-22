# 编写一个函数，该函数需要一个参数（文件名）并统计文件中单词的数量
def count_words(filename):
    """读取文件并返回单词数量，如果文件不存在则返回 None"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
        return None
    else:
        words = contents.split()
        return len(words)


# 阅读obama_speech.txt文件并计算单词数
# 阅读michelle_obama_speech.txt文件并计算单词数
# 阅读donald_speech.txt文件并计算单词数
# 阅读melina_trump_speech.txt文件并计算单词数

# 用列表存储所有文件路径，方便批量处理
speech_files = [
    './data/obama_speech.txt',
    './data/michelle_obama_speech.txt',
    './data/donald_speech.txt',
    './data/melina_trump_speech.txt',
]

# 遍历文件，统计并打印结果
for file_path in speech_files:
    word_count = count_words(file_path)
    if word_count is not None:
        print(f"There are {word_count} words in {file_path}.")
