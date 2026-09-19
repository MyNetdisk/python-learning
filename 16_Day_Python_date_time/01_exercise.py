from datetime import datetime

# 从datetime模块获取当前的日、月、年、小时、分钟和时间戳
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(f"Day: {day}, Month: {month}, Year: {year}, Hour: {hour}, Minute: {minute}, Timestamp: {timestamp}")

# 使用此格式格式化当前日期："%m/%d/%Y, %H:%M:%S"
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_date)

# 今天是2019年12月5日。将此时间字符串转换为时间。
date_string = "12/05/2019"
date_object = datetime.strptime(date_string, "%m/%d/%Y")
print(date_object)

# 计算现在和新年之间的时间差。
today = datetime.now()
new_year = datetime(today.year + 1, 1, 1)  # 动态计算下一年的1月1日，避免硬编码
time_difference = new_year - today
print(f"距离新年还有: {time_difference.days} 天")  # 用 .days 属性获取整数天数，更直观

# 计算1970年1月1日和现在之间的时间差。
time_since_epoch = today - datetime(1970, 1, 1)
print(f"自1970年1月1日以来: {time_since_epoch.days} 天")

# 思考，你可以将datetime模块用于什么？例如：
# 时间序列分析
# 获取应用程序中任何活动的时间戳
# 在博客上添加帖子
# 日志记录（每条日志带上时间戳便于排查问题）
# 定时任务（判断当前时间是否到达任务执行点）
# 缓存过期（计算缓存是否超过TTL）
# 生日/纪念日提醒（计算距离某个日期还有多少天）
