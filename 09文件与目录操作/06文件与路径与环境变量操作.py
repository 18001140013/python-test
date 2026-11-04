# # ========== 文件操作 ==========
# os.remove(file_name)           # 【文件操作】删除指定文件（不能删除目录）
# os.rename(old_name, new_name)  # 【文件/目录操作】重命名文件或目录
# os.path.isfile(path)           # 【文件操作】判断指定路径目标是否为文件
# os.path.splitext(path)         # 【文件操作】分离文件扩展名，返回 (文件名, 扩展名)
# os.path.basename(path)         # 【文件操作】提取文件名（含扩展名）
# os.path.getsize(path)          # 【文件操作】返回文件大小（字节）
#
# # ========== 路径操作（通用） ==========
# os.path.abspath(path)          # 【路径操作】获取指定相对路径的绝对路径（文件或目录均可）
# os.path.split(path)            # 【路径操作】分割路径为 (目录, 文件名) 元组
# os.path.exists(path)           # 【路径操作】判断指定路径是否存在（文件或目录均可）
# os.path.join(path, *paths)     # 【路径操作】连接多个路径片段，自动添加正确分隔符

# # ========== 环境变量获取 key-value ==========
# os.environ['JAVA_HOME']
# os.getenv('JAVA_HOME2')

# 文件操作
import os

# 获取当前目录
current_path = os.getcwd()
print(f'当前路径path:{current_path}')

# 指定当前目录
os.chdir(current_path)

# 创建一个测试目录
if not os.path.exists('test'):  # 判断当前路径是否不存在
    os.mkdir('test')  # 创建一个测试目录到当前文件夹

# 通过相对路径 获取到绝对路径 path
print(os.path.abspath('test/a.txt'))  # /Users/terminus/03_python/python_code/testpy_01/09文件与目录操作/test/a.txt

# 文件是否存在
print(f'是否为一个文件：{os.path.isfile('test/a.txt')}')

# 分隔函数1 （文件名、扩展名）
path_link = os.path.splitext(current_path + '/test/b.png')
print(path_link[0])  # /Users/terminus/03_python/python_code/testpy_01/09文件与目录操作/test/b
print(path_link[1])  # .png

# 分隔函数2 （目录、文件名）
path_link = os.path.split(current_path + '/test/a.txt')
print(path_link[0])  # /Users/terminus/03_python/python_code/testpy_01/09文件与目录操作/test
print(path_link[1])  # a.txt

# 提取文件名
file_name = os.path.basename(current_path + '/test/b.png')
# /Users/terminus/03_python/python_code/testpy_01/09文件与目录操作/test/b.png -> b.png
print(f'提取文件名:{file_name}')  # b.png

# 返回文件大小
file_size = os.path.getsize(current_path + '/test/a.txt')
print(f'获取文件大小:{file_size}')  # 8字节

# 修改文件名
old_name = current_path + '/test/c.mp4'
new_name = current_path + '/test/cc.mp4'

if not os.path.isfile(new_name):
    os.rename(old_name, new_name)
else:
    os.rename(new_name, old_name)

# 多个路径拼接自动增加：分隔符 os.sep
print(os.path.join('1', '2', '3'))  # 1/2/3

# 环境变量操作，后期可以通过环境变量 获取到大模型apiKey
# 以下2个函数都是获取当前环境变量key对应的value值 区别：获取不到会报错、不报错
print(os.environ['JAVA_HOME'])  # 如果不存在会报错
print(os.getenv('JAVA_HOME2'))  # 不存在时返回 None
