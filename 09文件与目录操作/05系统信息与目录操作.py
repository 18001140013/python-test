import os

# ========== 系统信息 ==========
# os.name                 # 【系统信息】查看当前操作系统名字，"nt"表示Windows，"posix"表示Linux
# os.sep                  # 【系统信息】获取当前系统平台路径分隔符
#
# # ========== 目录操作 ==========
# os.getcwd()             # 【目录操作】获取当前工作目录
# os.listdir(path)        # 【目录操作】列出指定目录path的所有文件和目录名
# os.chdir(path)          # 【目录操作】切换当前工作目录
#
# os.mkdir(path)          # 【目录操作】创建单层目录（父目录必须存在）
# os.makedirs(path)       # 【目录操作】创建多层目录（自动创建不存在的父目录）
#
# os.rmdir(path)          # 【目录操作】删除单层空目录（目录必须为空）
# os.removedirs(path)     # 【目录操作】递归删除多层空目录（从最内层开始），递归删除多层空目录，**从最内层往外层删**
# os.path.isdir(path)     # 【目录操作】判断指定路径目标是否为目录
# os.path.dirname(path)   # 【目录操作】提取路径中的目录部分


# 系统信息
print(f'系统名：{os.name}')  # posix 表示linux,nt表示 windows
print(f'路径分隔符：{os.sep}')  # 路径分隔符 mac: /

# 获取当前目录path
current_path = os.getcwd()
print(f'当前路径信息：{current_path}')  # 当前.py文件存放的目录

# 指定path下所有文件与目录的信息 以列表形式返回
print(f'当前路径下所有文件与目录信息：{os.listdir(current_path)}')  # 返回为列表

# 切换到指定目录
print(f'切换到指定path目录下：{os.chdir(current_path)}')

# 创建目录
try:
    print(f'在当前目录下创建一个目录：{os.mkdir('test')}')  # 在当前目录下创建目录，如果当前目录已存在会报错
    print(f'在当前目录下创建多层目录：{os.makedirs('test1/test2/test3')}')  # 在当前目录下创建多层目录，如果当前目录已存在会报错
except FileExistsError as fee:
    print(f'文件目录已经存在报错：{fee.strerror}')

# 判断目录是否存在
print(f'当前目录是否存在：{os.path.isdir('test')}')  # True
print(f'当前目录是否存在：{os.path.isdir('test1/test2/test3')}')  # True

# 获取上级目录path
print(f'提取指定path的父级路径：{os.path.dirname(current_path)}')

# 删除目录
print(f'{os.rmdir('test')}')  # 删除一个指定path的目录
print(f'{os.removedirs('test1/test2/test3')}')  # 删除一个指定path的多层目录
