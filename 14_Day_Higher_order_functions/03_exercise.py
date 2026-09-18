from collections import Counter
from data.countries_data import countries_data

# 使用 countries_data.py (https:countries-data.py) 文件，完成以下任务：
# 按国家名称、首都和人口排序国家
sorted_countries = sorted(countries_data, key=lambda country: country['name'])
print(sorted_countries)

sorted_countries_by_capital = sorted(countries_data, key=lambda country: country['capital'])
print(sorted_countries_by_capital)

sorted_countries_by_population = sorted(countries_data, key=lambda country: country['population'], reverse=True)
print(sorted_countries_by_population)


# 按位置排序出前十个最常用语言。
def most_spoken_languages(countries_data):
    all_languages = []
    for country in countries_data:
        all_languages.extend(country['languages'])
    language_counts = Counter(all_languages)
    return [lang for lang, _ in language_counts.most_common(10)]


print(most_spoken_languages(countries_data))


# 排序出前十个人口最多的国家。
def most_populous_countries(countries_data):
    return [country['name'] for country in sorted(countries_data, key=lambda c: c['population'], reverse=True)[:10]]


print(most_populous_countries(countries_data))
