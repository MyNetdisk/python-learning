# 为名为 countries_data.py 的文件中的数据创建一个名为 countries.py 的函数。
# 创建一个函数，找出十大使用的语言
from data.countries_data import countries_data


def most_spoken_languages(countries_data):
    """找出十大使用的语言，返回 [(语言名, 使用国家数), ...]"""
    # 用列表推导式展平所有语言列表
    all_languages = [lang for country in countries_data for lang in country['languages']]
    # Counter.most_common(10) 直接返回按频次降序的前10个 (元素, 频次) 元组
    from collections import Counter
    return Counter(all_languages).most_common(10)


# 打印结果时格式化输出
top_languages = most_spoken_languages(countries_data)
for rank, (lang, count) in enumerate(top_languages, 1):
    print(f"{rank}. {lang} - {count} 个国家使用")


# 创建一个函数，找出十大人口最多的国家
def most_populated_countries(countries_data):
    """找出十大人口最多的国家，返回 [(国家名, 人口数), ...]"""
    # 按人口降序排序，取前10，只提取国家名和人口数
    return [
        (country['name'], country['population'])
        for country in sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]
    ]


# 打印结果时格式化输出
top_countries = most_populated_countries(countries_data)
for rank, (name, pop) in enumerate(top_countries, 1):
    print(f"{rank}. {name} - {pop:,} 人")
