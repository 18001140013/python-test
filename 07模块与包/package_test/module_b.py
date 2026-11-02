__all__ = ["test1", 'b']  # 标示只将test1函数、b函数暴露出去
# __all__ 的控制，使用 from xx import *, 只能配合*这一种方式用

b = 200


def test1():
    print("test1")


def test2():
    print("test2")


def test3():
    print("test3")
