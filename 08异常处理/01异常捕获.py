# 异常捕捉与处理
# try: 异常代码块
# except: 若有异常会走最近的 except 处理代码
# except 异常type: 根据异常类型区别化处理，如果指定类型，没有指定的错误类型会报错出来。
# except Exception(父类)： 未知类型异常 兜底用的
a = 20
b = 0

try:
    print('1111')
    print(a / b)
    print('2222')

    raise Exception('主动抛出异常')  # 关键字 raise
# except:
#     print('程序有崩溃')
# except ZeroDivisionError:
#     print('被除数为0异常')
except ValueError:
    print('参数异常')
except Exception as e:
    print(f'异常信息： {e}')
    print(f'异常类型：{type(e)}')
    print(f'异常出现的文件： {e.__traceback__.tb_frame.f_code.co_filename}')
    print(f'异常出现具体的行数： {e.__traceback__.tb_lineno}')

    # 快捷方式打印异常的具体信息
    import traceback

    print(traceback.format_exc())
else:
    print('########## 没有异常时走的逻辑')
finally:
    print('########## 有没有异常都会走的逻辑')

print('后续代码111')
print('后续代码111')
print('后续代码111')
print('后续代码111')

''' 异常实战总结：

#### 步骤1：捕捉
try:  // 捕捉异常
    raise Exception('主动抛出异常') // 主动提出的异常

#### 步骤2：有异常情况处理
except:  // 处理异常
except ValueError: // 处理指定类型异常
except Exception as e: print(e) // 打印异常信息

#### 步骤3:无异常情况处理
else: 

#### 步骤4:有无异常情况都会进来
finally: 

'''
