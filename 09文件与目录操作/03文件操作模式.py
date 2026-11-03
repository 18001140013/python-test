#### open() 函数
# 模式都有：
# w 只写
# r 只读
# t 文本
# b 字节流
# a 追加，只用到写
# + 读与写
# r+ 读+写  // 不会清空原内容,写入会追加到尾部
# w+ 写+读 // 会先清空原来内容
# a+ 追加写+读 // 不会清空原来内容

# 读取内容，修改内容并写入到文件 使用：r+
fo = open(file='/Users/terminus/Autodesk/test3.txt', mode='r+', encoding='utf-8')
str = ''
while True:
    str_line = fo.readline()
    if str_line == '':
        break
    else:
        str += str_line

# 例1: 将字符替换、分隔、以列表形式追加到文件
# dfdsa、fdsfjdl、skfj // 1 line
# dfdsafdsfjdlskfj      // 2 line

# str = str.replace('f', 'F')  # 字符替换
# lis = str.split('、')  # 通过符号分隔成 列表
# print(lis)
# fo.write('\n')
# fo.writelines(lis)

# 例2：将old字符替换成 P,然后光标从头开始写，完成内容替换

str = str.replace('old', 'P')  # 字符替换
print(str)

fo.seek(0)  # 光标指向0

fo.write(str)  # 写入内容

fo.truncate() # 截掉重写后，多余的内容

# 关闭流
fo.close()
