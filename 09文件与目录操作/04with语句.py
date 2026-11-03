# with关键字用来简化文件的资源管理操作，用来自动释放资源，确保资源能被正确释放如：文件流、数据库连接断开、锁释放
# 简而言之：简化代码用来释放资源的
# 例子：完成 a->b文件的复制操作, 内容*10
with open('/Users/terminus/Autodesk/a.txt', 'wt', encoding='utf-8') as f:
    f.write('不见黄河之水天上来，奔流到海不复回。')

with (open('/Users/terminus/Autodesk/a.txt', 'rt', encoding='utf-8') as file1
    , open('/Users/terminus/Autodesk/b.txt', 'wt', encoding='utf-8') as file2):
    file2.write(file1.read() * 10)
