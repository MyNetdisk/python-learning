import random


# 编写一个函数 list_of_hexa_colors，它返回一个数组中的任意数量的十六进制颜色（六个十六进制数写在 # 后面。十六进制数字系统由 16 个符号组成，0-9 和 前 6 个字母 a-f。查看任务 6 的输出示例）。
def list_of_hexa_colors(n):
    hex_chars = "0123456789abcdef"
    hexa_colors = []
    for i in range(n):
        hex_code = ''.join(random.choices(hex_chars, k=6))
        hexa_colors.append(f'#{hex_code}')
    return hexa_colors


print(list_of_hexa_colors(5))


# 编写一个函数 list_of_rgb_colors，它返回一个数组中的任意数量的 RGB 颜色。
def list_of_rgb_colors(n):
    rgb_colors = []
    for i in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append(f'rgb({r}, {g}, {b})')
    return rgb_colors


print(list_of_rgb_colors(5))


# 编写一个函数 generate_colors，它可以生成任意数量的十六进制或 RGB 颜色。
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175)','rgb(50, 105, 100)','rgb(15, 26, 80)']
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Invalid color type. Please choose 'hexa' or 'rgb'."


print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))
