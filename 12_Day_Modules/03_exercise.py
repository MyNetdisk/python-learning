import random


# 调用你的函数 shuffle_list，它接受一个列表作为参数并返回一个打乱的列表。
# def shuffle_list(lst):
#     list_copy = lst.copy()
#     random.shuffle(list_copy)
#     return list_copy
def shuffle_list(lst):
    list_copy = lst.copy()
    shuffled = []
    while list_copy:
        idx = random.randint(0, len(list_copy) - 1)
        shuffled.append(list_copy.pop(idx))
    return shuffled


print(shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))


# 编写一个函数，它在 0-9 的范围内返回七个随机数的数组。所有数字必须是唯一的。
# def seven_random_numbers():
#     return random.sample(range(0, 10), 7)
def seven_random_numbers():
    result = []
    while len(result) < 7:
        num = random.randint(0, 9)
        if num not in result:
            result.append(num)
    return result


print(seven_random_numbers())
