# 从编程语言中提取所有Python目录文件：
# a) 处理30DaysOfPython文件夹，提取出所有python文件，并将它们的名称存储在files_list.txt文件中
import os


def find_python_files(directory):
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(file)
    with open('files_list.txt', 'w') as f:
        for file in python_files:
            f.write(file + '\n')


find_python_files('C:\\Users\\MyNetdisk\\Documents\\Project\\python-learning')

# b) 创建一个名为find_python.py的脚本，可以通过命令行运行它
# 见文件find_python.py
# c) 添加一个名为--version的标志来处理命令行参数
