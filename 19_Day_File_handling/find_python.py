# 从编程语言中提取所有Python目录文件：
# a) 处理30DaysOfPython文件夹，提取出所有python文件，并将它们的名称存储在files_list.txt文件中
# b) 创建一个名为find_python.py的脚本，可以通过命令行运行它
# c) 添加一个名为--version的标志来处理命令行参数

import os
import argparse


def find_python_files(directory):
    """递归查找目录下所有 .py 文件，并将相对路径写入 files_list.txt"""
    python_files = []
    # 获取目标目录的绝对路径，用于计算相对路径
    base_dir = os.path.abspath(directory)

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.py'):
                # 拼接完整路径
                full_path = os.path.join(root, file)
                # 计算相对于目标目录的路径（如 day1/main.py）
                rel_path = os.path.relpath(full_path, base_dir)
                python_files.append(rel_path)

    # 写入文件
    output_file = 'files_list.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        for file_path in python_files:
            f.write(file_path + '\n')

    print(f"找到 {len(python_files)} 个 Python 文件，已保存到 {output_file}")
    return python_files


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='查找指定目录下的所有 Python 文件')
    parser.add_argument('directory', help='要搜索的目录路径')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()

    # 验证目录是否存在
    if not os.path.isdir(args.directory):
        print(f"错误：目录 '{args.directory}' 不存在或不是有效目录。")
    else:
        find_python_files(args.directory)
