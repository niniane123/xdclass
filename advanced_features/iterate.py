# 判断是否是可迭代对象 isinstance()
from collections.abc import Iterable

# Return whether an object is an instance of a class or of a subclass thereof.
print(isinstance(range(10), Iterable))

print(isinstance(list(range(10)), Iterable))

print(isinstance({"name": "zhangrenchao"}, Iterable))

print(type({"name"}))

# list中迭代的简便方法
list_b = [[1, 2], [2, 4], [6, 8, 89]]
for ele, mem in list_b:
    print(ele + mem)
