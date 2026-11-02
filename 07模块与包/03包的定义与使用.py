# 一个文件夹做为一个包，包含了一整块模块或子包，一个包下会有一个__init__.pyth 文件

######### 使用1
# 在这里测试一下 包的引入
import package_test.module_a  # 方式1
import package_test.sub_package_test.module_c  # 方式1

print(f'访问变量a：{package_test.module_a.a}')
print(f'访问变量c：{package_test.sub_package_test.module_c.c}')

######### 使用2
from package_test.sub_package_test.module_d import d  # 方式2
from package_test.sub_package_test.module_d import d as t_d  # 方式2

print(f'访问变量d：{d}')
print(f'访问变量d：{t_d}')

from package_test.module_b import *  # 方式导入 模块所有

print(f'访问变量b：{b}')
test1()

######### 使用3
import package_test.sub_package_test.module_test as md_test  # 导入模块 指定名为 md_test

print(f'访问变量num_test: {md_test.num_test}')
md_test.func_test1()
md_test.func_test2()
