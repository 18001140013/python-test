# 原来装饰器都是以函数形式定义的，这里以类的形式完成装饰器的使用
# 装饰器类：
# 1 构造函数必须有fun
# 2 重写 __call__ 方法，这个方法就是内部函数：inner
import time


# 登录装饰器
class Login:
    def __init__(self, func):
        self.func = func

    # 这里的call就是 inner 函数
    def __call__(self, *args, **kwargs):
        # 去做登录操作
        print(f'登录成功！！！')
        time.sleep(1)
        # 调用函数
        return self.func(*args, **kwargs)


# 定义评论函数
@Login
def comment(name):
    print(f'用户 {name} 评论成功')


# 测试
if __name__ == '__main__':
    comment('李四')
