######## 函数定义
# 函数定义：组织好，后期重复调用
# def , python中没有大括号{}
# 先定义后使用

# def 定义函数， 箭头后面为：返回参数
def show_java_plan(name) -> int:
    '''一句话描述函数

    详细说明：逻辑

    :param name:
    :return:
    '''
    print(f"{name} 打电话")
    return 0


#  函数调用
print(show_java_plan('小明'))
