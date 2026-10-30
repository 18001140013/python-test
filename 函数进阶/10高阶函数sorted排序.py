# 排序函数：sorted
# 语法：sorted(list,key=func(a),reverse)->list

# 1、数字数据
list1 = [1, 20, 3, 40, 5]
print(sorted(list1))  # 升序 1、3、 5、 20、 40
print(sorted(list1, reverse=True))  # 降序 40、20、5、3、1


# key: 通过一个函数返回排序的值
# 例子：
def func1(x):
    print(f'来了 {x}')
    return x


print(f"自定义排序1 {sorted(list1, key=func1)}")
print(f"自定义排序2 {sorted(list1, key=lambda x: -x)}")

# 2、对象数据
list2 = [{'name': '小明', 'age': 18, 'sex': 1},
         {'name': '小强', 'age': 20, 'sex': 1},
         {'name': '小丽', 'age': 16, 'sex': 2},
         ]


# 根据年龄升序排序 小丽 < 小明 < 小强
def func2(item):
    print(f'item=== {item}')
    return item['age']


print(f"自定义排序3 {sorted(list2, key=func2)}")
print(f"自定义排序4 {sorted(list2, key=lambda item: item['age'])}")

# 根据length长度升序
list3 = ['aaaaaaaaa', 'a', 'aaaa', 'aaaaaaa', 'aa']
print(f"自定义排序4 {sorted(list3, key=lambda str: len(str))}")
# 简写 直接给len函数，所以key=func(item) ,必须是一个函数
print(f"自定义排序5 {sorted(list3, key=len)}")
