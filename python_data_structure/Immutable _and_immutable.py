# 可变对象 可以改变对象在内存中的值,但是内存地址不会变 id()函数计算结果不变
# 数字类型不可变
# 常见的不可变类型：数字、字符串、元组
a = 1
print(id(a))
a = a + 2
print(id(a))

# list类型为可变对象或者数组 内存中对象的值改变，对象的内存地址不泛生改变
# 常见的可变类型 list/dic
b = [1, 2, 3, 4]
print(id(b))
b.append(7)
print(id(b))

tuple_a = (1, 2, 3, [1, 2, 34, 5])
print(tuple_a)
tuple_a.__getitem__(-1).__setitem__(0, 2)
print(tuple_a)
