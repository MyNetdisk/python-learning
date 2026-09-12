import random
import string


# 编写一个生成六位数/字符 random_user_id 的函数。
#   print(random_user_id());
#   '1ee33d'
def random_user_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))


print(random_user_id())


# 修改上一个任务。声明一个名为 user_id_gen_by_user 的函数。它不接受任何参数，但接受两个输入。一个输入是字符的数量，另一个输入是应生成的 ID 数量。
# print(user_id_gen_by_user()) # 用户输入：5 5
# #输出：
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf
#
# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr
def user_id_gen_by_user():
    char_length = int(input("请输入字符数量: "))
    id_length = int(input("请输入生成数量: "))
    # 字符集包含大写字母、小写字母和数字
    chars = string.ascii_letters + string.digits
    user_ids = []
    for i in range(id_length):
        user_ids.append(''.join(random.choices(chars, k=char_length)))
    return '\n'.join(user_ids)


print(user_id_gen_by_user())


# 编写一个名为 rgb_color_gen 的函数。它将生成 RGB 颜色（每个值范围从 0 到 255）。
# print(rgb_color_gen())
# # rgb(125,244,255) - 输出应该是这种形式
def rgb_color_gen():
    return f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'


print(rgb_color_gen())
