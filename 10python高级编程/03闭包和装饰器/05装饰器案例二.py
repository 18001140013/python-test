# 案例二：给多个函数增加一个：账号登录扩展
# 实战：给装饰器传参数
# 普通装饰器与带参装饰器区别：普通为2层函数嵌套，带参为3层函数嵌套->会将装饰器作为参数返回
# 需求：
# 1 先判断是否已经登录，如果已登录则执行外调函数，反之：需要输入账号密码校验登录，
# 2 如果从未有过账号录入，则需要录入账号与密码
# 3 一条账号与密码为一条字符串信息存放于本地文件中
import os.path


# 定义代参数的装饰器函数
# 一层：用来接受参数
# ===================注意：程序加载时执行：一层函数代码
def login(user_path):
    print(f'一层函数代码已执行 ->收到参数：{user_path}')

    # 二层：装饰器
    # ===================注意：程序加载时执行：二层函数代码
    def login_decorator(func):
        print(f'二层函数代码已执行 ->用户数据读取')

        is_login = False  # 是否已经登录

        user_lis = []  # 1读取所有用户数据
        if not os.path.exists(user_path):
            choice = input('目前还没有账户，是否要创建（y/n）:')
            if choice == 'y' or choice == 'Y':
                username = input('请录入您的账号：')
                password = input('请录入您的密码：')
                user = {'username': username, 'password': password}

                line_str = str(user) + '\n'  # 对象转str：{'username': 'lisi', 'password': '123'}

                open(user_path, 'w', encoding='utf-8').write(line_str)

                user_lis.append(user)
            else:
                print('程序正常退出！')
                exit(0)
        else:
            with open(user_path, 'r', encoding='utf-8') as f:
                list_line = f.readlines()
                for line in list_line:
                    user_lis.append(eval(line))  # eval函数： 会将str格式转为dict类型

        # 三层：内部函数
        # ===================注意：三层函数代码在 test() 函数调用后才会执行
        # 定义处：`*` `**` 是打包：把进来的参数打包成元组、字典
        def inner(*args, **kwargs):  # 万能参数，适配任意函数
            print("====调用前日志====")
            print(f"位置参数 args：{args}")
            print(f"关键字参数 kwargs：{kwargs}")

            print(f'三层函数代码已进来 ->账户验证中...')

            nonlocal is_login  # 标识为外部函数变量

            if not is_login:
                # 2进行登录与验证
                user_name = input('请输入您的账号：')
                pass_word = input('请输入您的密码：')
                for item in user_lis:
                    if item['username'] == user_name and item['password'] == pass_word:
                        is_login = True
                        print(f'欢迎 {user_name} 登录进来!')
                        break

            # 3执行函数
            if is_login:
                # 调用处：`*` `**` 是解包：把元组、字典拆开，传给原函数
                return func(*args, **kwargs)

            return '没有找见您的账号，程序结束！'

        return inner

    return login_decorator


# 这里注解定义，会在代码加载时执行 一层、二层函数，然后得到inner函数，待test函数执行时，其实执行的是inner函数，然后再在内部回调test函数，才是真的test()执行
@login('user.txt')  # 这里的注解会在代码加载时，自动执行 login() 函数程序
def test(a, b, c):
    print(f'业务函数 test() 已执行！！！{(a + b + c)}')
    return '返回值'


# 测试代码
if __name__ == '__main__':
    print('代码测试开始====== 》')
    print(f'test1函数测试：{test(1, b=2, c=3)}')
    print(f'test2函数测试：{test(4, 5, 6)}')
    print(f'test3函数测试：{test(7, 8, 9)}')
    print('代码测试结束====== 》')
