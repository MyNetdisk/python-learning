# 1、以下是 10 个学生的年龄列表：
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 对列表进行排序，并找出最大和最小年龄
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"最小年龄: {min_age}, 最大年龄: {max_age}")

# 将最小年龄和最大年龄再次添加到列表中
ages.append(min_age)
ages.append(max_age)
print(f"添加后: {ages}")

# 找到年龄中位数
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:
    median_age = ages[n // 2]
print(f"中位数: {median_age}")

# 找到平均年龄
average_age = sum(ages) / len(ages)
print(f"平均年龄: {average_age}")

# 找到年龄范围
age_range = max_age - min_age
print(f"年龄范围: {age_range}")

# 比较 (min - average) 和 (max - average) 的值
diff_min = abs(min_age - average_age)
diff_max = abs(max_age - average_age)
print(f"|min - average| = {diff_min}")
print(f"|max - average| = {diff_max}")
print(f"两者是否相等: {diff_min == diff_max}")

# 在国家列表中查找中间的国家
countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola',
    'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria',
    'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados',
    'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan',
    'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei',
    'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon',
    'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile',
    'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo',
    'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus',
    'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
    'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
    'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland',
    'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany',
    'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea',
    'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary',
    'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq',
    'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan',
    'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North',
    'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia',
    'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
    'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi',
    'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
    'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova',
    'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar',
    'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand',
    'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman',
    'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay',
    'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar',
    'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
    'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
    'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore',
    'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa',
    'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland',
    'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan',
    'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago',
    'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda',
    'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay',
    'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam',
    'Yemen', 'Zambia', 'Zimbabwe',
]

mid = len(countries) // 2

if len(countries) % 2 == 0:
    middle_country = countries[mid - 1:mid + 1]
else:
    middle_country = countries[mid]

print(f"中间的国家: {middle_country}")

# 将国家列表分成两个相等的列表（奇数时第一个半多一个国家）
split_point = (len(countries) + 1) // 2
first_half = countries[:split_point]
second_half = countries[split_point:]
print(f"前半部分数量: {len(first_half)}, 后半部分数量: {len(second_half)}")

# 拆解前三个国家和剩下的北欧国家
countries1 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_three_countries = countries1[:3]
northern_europe_countries = countries1[3:]
print(f"前三个国家: {first_three_countries}")
print(f"北欧国家: {northern_europe_countries}")
