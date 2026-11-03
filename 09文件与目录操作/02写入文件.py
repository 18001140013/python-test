# 将内容写入到文件
# fo = open(file,mode='wt',encoding='utf-8') mode:at 写入追加、wt:清空并写入
# fo.write('123') # 将内容写入到缓存区
# fo.flush() // 将缓存区的内容更新到文件中
# fo.close() # 关闭流

#  打开文件、创建流对象
fo = open(file='/Users/terminus/Autodesk/test2.txt', mode='at', encoding='utf-8')
fo.write('写入123456890')
fo.flush()
fo.close() # 如果不用flush函数时，close调用时内部会先将缓存写到文件再关闭
