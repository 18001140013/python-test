# 装饰器的定义：不修改已有的函数源代码、给已经有函数增加额外的功能，也叫功能扩展
# 这个扩展功能就是装饰器，本质上也是一个闭包函数

# 给评论增加一个扩展功能-登录，评论之前先登录
def comment():
    print('=======评论')


# 装饰器的第一个参数必须是一个函数
def login_comment(func):
    def inner():
        print('=======登录')
        func()  # 执行外部函数

    return inner


# 装饰器标记，将login_comment函数扩展给comment2
@login_comment
def comment2():
    print('=======评论')


# 测试
if __name__ == '__main__':
    # 方式1:
    lc = login_comment(comment)
    lc()  # 此时这个lc即为 内部函数：inner

    # 方式2:
    comment2()  # 装饰函数更加简单的用法： @装饰器名字，可以完成对已有函数的装饰
