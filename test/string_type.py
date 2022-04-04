# 字符串的不不变性，一旦改变了字符串会重新分配内存空间
name = "zrc1997"
print(id(name))
name = "zhangrenchao"
print(id(name))

# 字符串的单引号、双引号、三引号、转义字符的使用场景
I_am_so_lucky1 = 'I\'m so lucky1'
print(I_am_so_lucky1)
I_am_so_lucky2 = "I'm so lucky2"
print(I_am_so_lucky2)
print('他说:"我很好"')
# 三引号的使用场景 ——可以换行
print('''
四川
成都  
都江堰

''')
# 转义字符
print('\a')

# 字符串拆分
a = 'my name is zhang ren chao '
# 获取指定索引下的字符串
print(a[0])
# print(a[100])

# 从后往前数
print("导数第一个字母是" + a[-1])

# 获取指定索引范围内的一段字符串;左闭右开的取
print(a[0:2])

# 获取整个字符串
print(a[0:-1])
print(a[0:])
print(a[:3])

# 占位符的使用

