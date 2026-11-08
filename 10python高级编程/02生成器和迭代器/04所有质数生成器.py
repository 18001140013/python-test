# 实现质数生成器：可以无限的取出质数
# 质数：一个自然数只有2个因数 而是：1和自己
# 合数：一个自然数有3个或以上个因数

def generator_func():
    number = 2
    yield number
    while True:
        number += 1  # 不断向下+1

        for j in range(2, number):
            if number % j == 0:  # 除以所有比自己小的、非1 自然数，如果还有被整出的数，说名是一个合数
                break
        else:
            yield number


# 测试 打印100内的所有质数
if __name__ == '__main__':
    gf = generator_func()
    number = 100
    for item in gf:
        result = item
        if result > number:
            gf.close()
            break
        else:
            print(result)
