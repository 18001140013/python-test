# filter函数 过滤数据用的, 与map的用法一样
# 语句：filter(function(a),list) => filter对象
# list -> function(item) -> new_list

lis = [1, 2, 3, 4, 5]


# 筛选出偶数来
def func(item):
    print(f'item={item}')
    return item % 2 == 0


result = filter(func, lis)
result2 = filter(lambda x: x % 2 == 0, lis)

print(f'type={type(result)},value={result}')
print(f'type={type(result2)},value={result2}')

print(list(result))  # [2,4] 转换时才执行函数处理程序 走func
print(list(result))  # 仅一次函数加工，之后不再走 结果： []
print(list(result2))  # [2,4]
