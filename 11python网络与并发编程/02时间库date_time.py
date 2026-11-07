from datetime import date  # 日期
from datetime import time  # 时间
from datetime import datetime  # 日期 + 时间
from datetime import timedelta  # 时间差

# 功能更强大，默认时区为北京时间东八区

# datetime 模块的五大类：
# 1. datetime.date：表示日期的类，主要用于处理年、月、日；
# 2. datetime.time：表示时间的类，主要用于处理时、分、秒；
# 3. datetime.datetime：表示日期时间的类，date 类和 time 类的综合使用，可以处理年、月、日、时、分、秒；
# 4. datetime.timedelta：表示时间间隔，即两个时间点的间隔，主要用于做时间加减的
# 5. datetime.tzinfo：时区的相关信息。

####### 日期对象 date
current_date = date.today()
print(f'=====[date] {type(current_date)} 当前时间：{type(current_date)}, {current_date}')
current_date2 = date(2019, 11, 2)
print(f'=====[date] 指定的时间：{current_date2}')
print(f'=====[date] 转格式：{current_date2.strftime("%Y.%m.%d")}')
print(f'=====[date] 时间元组对象：{current_date.timetuple()}')
print(f'=====[date] 年、第几周、这周的第几天：{current_date.isocalendar()}')

####### 时间对象 time
current_time = time(18, 30)
print(f'=====[time] ：{current_time}')

########## 时间差对象：timedelta ,对时间加减
# 后2天
data3 = datetime.now() + timedelta(days=2)
print(f"=====[datetime] {type(data3)} {data3}")

# 前2天
data4 = datetime.now() - timedelta(days=2)
print(f"=====[datetime] {type(data4)} {data4}")

# 解析时间
start = datetime.strptime('2026.11.7 18:50:00', '%Y.%m.%d %H:%M:%S')
end = datetime.strptime('2026.11.10  18:55:00', '%Y.%m.%d %H:%M:%S')

r = end - start  # 差对象
# timedelta
print(f"=====[timedelta] {type(r), r.days, r.seconds}")  # 差

# dateTime 年中的日
print(f'=====[dateTime] 当前是年中的第多少天 {type(start)} {start.strftime('%j')} 方法2:{start.timetuple().tm_yday}')

# 上月最后一天
td = date.today()
p_month_end_day = date(year=td.year, month=td.month, day=1) - timedelta(days=1)
print(f"=====[date] 上月最后一天: {p_month_end_day}")
