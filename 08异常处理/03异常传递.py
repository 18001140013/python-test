def test1():
    print('test1开始')
    print('test1结束')


def test2():
    print('test2开始')
    # 从这里捕捉最靠谱，程序异常，不会中断其他程序执行
    try:
        a = 3 / 0  # 制造异常，报错后程序中断执行
    except Exception as result:
        print(f'test1 {result}')

    test1()
    print('test3结束')


def test3():
    print('test3开始')
    # 这里捕捉，也会影响部分程序中断
    try:
        test2()
        print('=======test2函数后面程序')
    except Exception as result:
        print(f'test2 {result}')

    print('test3结束')


if __name__ == '__main__':
    # 从这里捕捉：异常抛出后，捕捉打印，后面程序不会再执行了，所以需要去报错的地方去捕捉，才能使得程序正常执行
    try:
        test3()
        print('=======test3函数后面程序')
    except Exception as result:
        print(result)
