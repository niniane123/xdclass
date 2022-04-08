# 列表 list[]
# list的存储结构：存放的是对象的指针对象， 指针指向真正的元素。因为指针的存在，python的效率有所提高
# list中成员可以重复出现
# 增删改查操作
list_a = [1, 2, 3]
print(list_a)
print(type(list_a))

# python的API

# 队列尾部添加元素
list_a.append(4)
print(list_a)

# 队列中间的某个位置添加元素
list_a.insert(1, 66)

# 删除队列中的某个元素
list_a.__delitem__(0)
print(list_a)

# 查看队列的长度  3
print(len(list_a))

# 查看队列中的某一个元素,倒数第几个数
print(list_a.__getitem__(2))
print(list_a.__getitem__(-1))

# 查看队列中某个元素的索引位置，存在会返回索引位置，不存在运行的时候程序会报错。
print(list_a)
print(list_a.index(2))

# 查看列表的长度
print(len(list_a))

# 弹出元素          Remove and return item at index (default last).
print(list_a)
#  参数为index
item = list_a.pop(2)
print(item)
print(list_a)

# 成员可以重复出现         """ Insert object before index. """
list_a.insert(20, 4)
print(list_a)
