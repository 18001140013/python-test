########## 模块导入使用：如果导入进来没用 颜色会变成灰色
# import my_mod #方式1： 整个文件
from my_mod import test  # 方式2：指定一个函数，适合部分引用
# import my_mod as tm  # 方式3: 给模块起个别名
# from my_mod import t_number as tn  # 方式4：只导入一个变量
from my_mod import *  # 方式5：导入所有

# my_mod.test(6, 4)# 方式1
test(6, 4)  # 方式2
# tm.test(5, 5)  # 方式3
# print(tn)  # 方式4
print(t_number)  # 方式5
