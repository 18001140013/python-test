# 迭代器：为for循环提供快捷遍历
# 迭代器的定义为3个条件：
# 1 __iter__ __next__ 函数
# 2 __iter__() 必须返回 对象 self
# 3 __next__() 必须返回 下一条数据
from collections.abc import Iterator


# 迭代器对象也叫迭代对象也是可迭代对象，我们实现一个Range函数
# * 后面参数赋值 必须要用形参名
# / 前面参数赋值 必须禁用形参名
class MyRange:
    def __init__(self, *, start, end):
        print('=====[init]')
        self.num = start - 1
        self.end = end

    def __iter__(self):
        print('=====[iter]')
        return self

    def __next__(self):
        print('=====[next]')
        self.num += 1
        if self.num >= self.end:
            raise StopIteration
        return self.num


if __name__ == '__main__':
    my_range = MyRange(start=0, end=6)
    # type 查看对象属于哪个类
    # isinstance 判断对象是否属于某个类
    print(f'type={my_range}, is Iterator 是否为一个迭代器={isinstance(my_range, Iterator)}')

    # for 遍历时 会先调用iter函数获取self,然后内部不断调用next函数直到 StopIteration异常停止循环
    for item in my_range:
        print(f'遍历：{item}')
