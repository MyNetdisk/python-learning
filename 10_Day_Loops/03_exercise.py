# ============================================================
# 优化后的完整代码 — 对应 10_Day_Loops 第24天练习
# 尽量使用 for / while 循环实现，适合循环练习
# ============================================================

from data.countries import countries
from data.countries_data import countries_data

# ----------------------------------------------------------
# 任务1: 循环遍历所有国家，提取出所有包含字母 "land" 的国家
# ----------------------------------------------------------
land_countries = []
for country in countries:
    # 用 .lower() 转小写，避免大小写遗漏
    if 'land' in country.lower():
        land_countries.append(country)

print("包含 'land' 的国家:")
for c in land_countries:
    print(f"  {c}")
print(f"  共 {len(land_countries)} 个\n")

# ----------------------------------------------------------
# 任务2: 使用循环反转列表中的元素
# ----------------------------------------------------------
fruits = ['banana', 'orange', 'mango', 'lemon']

# 倒序遍历，逐个放入新列表
reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print("反转后的列表:", reversed_fruits)
# 输出: ['lemon', 'mango', 'orange', 'banana']

# ----------------------------------------------------------
# 任务3: 数据中一共有多少个不重复的语言？
# ----------------------------------------------------------
languages = []
for country in countries_data:
    if country.get('languages'):
        languages.extend(country.get('languages'))

# 手动去重（不用 set，用循环实现）
unique_languages = []
for lang in languages:
    is_new = True
    for existing in unique_languages:
        if lang == existing:
            is_new = False
            break
    if is_new:
        unique_languages.append(lang)

print(f"\n共有 {len(unique_languages)} 种不重复的语言:")
# 手动排序（不用 sorted，用冒泡排序）
for i in range(len(unique_languages)):
    for j in range(len(unique_languages) - 1 - i):
        if unique_languages[j] > unique_languages[j + 1]:
            unique_languages[j], unique_languages[j + 1] = unique_languages[j + 1], unique_languages[j]

for lang in unique_languages:
    print(f"  {lang}")

# ----------------------------------------------------------
# 任务4: 找到被最多国家使用的语言
# ----------------------------------------------------------
most_spoken_languages = {}
for country in countries_data:
    for lang in country.get('languages', []):
        most_spoken_languages[lang] = most_spoken_languages.get(lang, 0) + 1

# 手动按值降序排序（不用 sorted + lambda，用冒泡排序）
items = list(most_spoken_languages.items())
for i in range(len(items)):
    for j in range(len(items) - 1 - i):
        if items[j][1] < items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

print(f"\n被最多国家使用的语言（前5名）:")
for idx in range(min(5, len(items))):
    lang, count = items[idx]
    print(f"  {lang}: {count} 个国家")

# ----------------------------------------------------------
# 任务5: 找到人口排名前十的国家
# ----------------------------------------------------------
# 手动提取所有国家信息
all_countries_info = []
for country in countries_data:
    all_countries_info.append({
        'name': country.get('name'),
        'population': country.get('population')
    })

# 手动按人口降序排序（不用 sort + lambda，用冒泡排序）
for i in range(len(all_countries_info)):
    for j in range(len(all_countries_info) - 1 - i):
        if all_countries_info[j]['population'] < all_countries_info[j + 1]['population']:
            all_countries_info[j], all_countries_info[j + 1] = all_countries_info[j + 1], all_countries_info[j]

# 取前10
print(f"\n人口排名前十的国家:")
for idx in range(min(10, len(all_countries_info))):
    item = all_countries_info[idx]
    print(f"  {idx + 1}. {item['name']} - 人口: {item['population']:,}")
