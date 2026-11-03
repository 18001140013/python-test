# 建立一个管子桥梁，去吸取文件里面的内容到内存中
# 函数为：open

#  打开文件、创建流对象
ob = open('/Users/terminus/Autodesk/test.txt', mode='rt', encoding='utf-8')
# str = ob.read()  # 读取文件内所有的内容
# str = ob.readline() # 读取文件1行的内容
# str = ob.read(30)  # 读取30个文字
str_lis = ob.readlines()  # 读取所有行内容，返回为一个列表

print(f'所有内容：{str_lis}')

# 多次读取文件内所有的内容
while True:
    str_line = ob.readline()
    if str_line != '':
        print(f'循环读：{str_line}', end='')
    else:
        break

# 关闭流
ob.close()
