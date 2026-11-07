# 2个时间库： time、datetime
import time # 默认时区为：格林威治时区

# 时间戳：距离格林威治时间1970年1月1日00:00至今的秒数就是时间戳，北京东8区，1970年1月1日08:00
print(f'当前时间戳：{time.time()}')  # 1793873812.022722 小数点后面为：毫秒与微秒

# 当前时间戳对应的西方国家习惯的时间格式 Thu Nov  5 18:18:05 2026
print(time.ctime())
# 元祖格式时间：time.struct_time(tm_year=2026, tm_mon=11, tm_mday=5, tm_hour=10, tm_min=18, tm_sec=49, tm_wday=3, tm_yday=309, tm_isdst=0)
gm_time = time.gmtime()
print(gm_time)
print(f'年：{gm_time.tm_year}')
print(f'月：{gm_time.tm_mon}')
print(f'日：{gm_time.tm_mday}')
print(f'一年中第几天：{gm_time.tm_yday}')

print(f'时：{gm_time.tm_hour}')
print(f'分：{gm_time.tm_min}')
print(f'秒：{gm_time.tm_sec}')

# 时间戳转元祖格式
gm_time2 = time.gmtime(1793873812)
print(f'时间戳转元祖格式:{gm_time2}')

# 转换为本地时间
print(f'本地时间:{time.localtime()}')

# 时间格式化函数：format 参数指定的字符串, 见：2026-11-05 18:43:15
print(f'format格式化函数：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}')

# 时间解析函数：将指定的格式时间转为元祖格式
p_time = time.strptime('2026年11月05日 18:43:15', '%Y年%m月%d日 %H:%M:%S')
print(f'时间解析函数:{p_time}')
