import pandas as pd

# 阅读hacker_news.csv文件并获取前五行
df = pd.read_csv('hacker_news.csv')
print(df.head())

# 获取标题列
titles = df['title']
print(titles)

# 获取行数、列数
num_rows, num_cols = df.shape
print(f"Number of rows: {num_rows}, Number of columns: {num_cols}")

# 获取前十行和最后十行
# print(df.iloc[0:10])
# print(df.iloc[-10:])

print(df.head(10))
print(df.tail(10))

# 获取第二行和第四行从第二列到第四列的数据
print(df.iloc[1:4, 1:4])

# 获取主题为Python的行
python_rows = df[df['title'].str.contains('Python', case=False)]
print(python_rows)

# 获取Python主题行的数量
num_python_rows = python_rows.shape[0]
print(f"Number of Python rows: {num_python_rows}")

# 获取投票数超过200的所有行
high_voted_rows = df[df['num_points'] > 200]
print(high_voted_rows)

# 按投票数排序数据框
sorted_df = df.sort_values(by='num_points')
print(sorted_df)

# 按投票数进行降序排序
sorted_df_desc = df.sort_values(by='num_points', ascending=False)
print(sorted_df_desc)

# 过滤掉Python主题并按票数排序
filtered_df = df[(df['title'].str.contains('Python', case=False)) & (df['num_points'] > 200)]
print(filtered_df)
