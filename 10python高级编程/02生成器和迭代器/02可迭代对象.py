# 可迭代对象：__iter__ 函数必须返回 可迭代对象即为 可迭代对象
# 迭代器器属于可迭代对象
# 迭代器对象是可迭代对象，可迭代对象不是迭代器对象
# 区别：迭代器对象 有__iter__ __next__函数，可迭代对象只有__iter__函数
# 迭代器对象占用内存永远只有一个空间，迭代完成后会释放掉
# range() // 属于可迭代对象
# list、dict、set、对象、字符串、tuple 都可以遍历，都属于可迭代对象

# 定义一个可迭代对象
class IterRange:

    def __init__(self, *, start, end):
        self.range = MyRange(start=start, end=end)

    def __iter__(self):
        return self.range

    pass


# 定义迭代器对象
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

    pass


from collections.abc import Iterator, Iterable

if __name__ == '__main__':
    iter_range = IterRange(start=0, end=6)
    my_range = MyRange(start=0, end=6)
    # 判断是否为迭代器对象
    print("[判断是否为迭代器对象:]")
    print(isinstance(iter_range, Iterator))  # false
    print(isinstance(my_range, Iterator))  # True
    print(isinstance([1, 2, 3], Iterator))  # false

    # 判断是否为可迭代对象
    print("[判断是否为可迭代对象:]")
    print(isinstance(iter_range, Iterable))  # True
    print(isinstance(my_range, Iterable))  # True
    print(isinstance([1, 2, 3], Iterable))  # True

    # 说名迭代器也是一个可迭代对象
    # Iterator is Iterable
    # 1遍历时会先通过__iter__获取到 迭代器对象
    # 2拿到迭代器对象不断调用next去遍历，知道StopIteration
    for item in iter_range:
        print(item)

    # 优势：永远只占用一个空间内存，大数据遍历比较适合
    # 缺点：没有索引，不适合指定查询、删除、修改
