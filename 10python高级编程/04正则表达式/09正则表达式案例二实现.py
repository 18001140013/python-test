# 案例一匹配QQ号码
# 要求：5-11全是数字，首位不能是0
import re

QP = r'^[1-9]\d{4,10}$'


def check(pattern, str):
    result = re.match(pattern, str)
    print(result)
    return result


# 测试
if __name__ == '__main__':
    check(QP, '1234556789000111')
    check(QP, '88888')
    check(QP, '099999988888')
    check(QP, '1250776814')
