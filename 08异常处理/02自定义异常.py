# 自定义一个异常类型 继承Exception,类名一般Error 结尾
class WeightError(Exception):

    def __init__(self, value):
        self.value = value  # 扩展对象属性使用
        super().__init__('传参:' + value)  # 入参时可以修改报错内容

    def __str__(self):
        # return f'异常原因：自自定义报错!!!'  # 返回异常基本信息
        return f'异常原因：自自定义报错 {self.value}!!!'  # 返回异常基本信息


# 测试异常
def test():
    w = int(input('输入重量:'))
    if w > 200:
        raise WeightError('重量超标了！！')
    else:
        print(w)


if __name__ == '__main__':
    try:
        test()
    except Exception as result:
        import traceback  # 可以打印出多有异常

        print(f'异常结果1：{result}')
        print(f'异常结果2：{traceback.format_exc()}')
