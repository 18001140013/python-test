# 案例一匹配账号与密码
# 要求：
# 1 用户名只能包含数字、字母、下划线
# 2 不能以数字开头
# 3 长度在6-16范围
# 4 密码不能包含符号：!@#$%^&*
import re

UP = r'^[a-zA-Z]\w{5,15}$'
PP = r'^[a-zA-Z][^!@#$%^&*]{5,15}$'


def check(pattern, str):
    result = re.match(pattern, str)
    print(result)
    return result


def start(u, p):
    if check(UP, u) is None:
        print('账号格式有误请重新输入')
    elif check(PP, p) is None:
        print('密码格式有误请重新输入')
    else:
        print('恭喜录入成功！！！')


if __name__ == '__main__':
    check(UP, 'jian')
    check(UP, '0huahua')
    check(UP, 'huahua')
    check(UP, 'HHHHHH')

    check(PP, 'HHHHHH[')
    check(PP, 'HHHHHH!')
    check(PP, 'HHH@HHH')
    check(PP, 'HHHHHH)')

    # u = input('请录入您的账号：')
    # p = input('请录入您的密码：')
    # start(u, p)
