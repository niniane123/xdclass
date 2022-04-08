# set集合 无序，存放的顺序可能和数据结构中实际的数据不相同
# 集合的生成方式；{1,2,3}， set()函数用于生成一个空的集合，{}表示生成一个空的字典

# 增
# add函数()
set_a = set()
set_a.add(1)
print(set_a)

# union函数() 返回一个新的set值;
# Return the union of sets as a new set.
set_b = {2, 3, 4, 5, 65, 6}
set_c = set_a.union(set_b)
print("set_a为" + set_a.__str__())
print("set_b为" + set_b.__str__())
print("set_c为" + set_c.__str__())

# 删  参数element 而非index
# 使用remove();存在则移除，不存在则报错
set_a.remove(1)
print(set_a)

# 使用discard()移除，存在则移除，不存在不报错
set_a.discard(300)
print(set_a)

# 使用pop随即弹出并且删除一个元素
# Remove and return an arbitrary set element.
# Raises KeyError if the set is empty.
# set_a.pop()

# clear()清空集合
set_a.clear()

# 改
# """ Update a set with the union of itself and others. """
set_a.update([1, 2, 3])
print(set_a)

# 查
# set的无序性  {8, 6, 7}
set_d = {6, 7, 8}
print(set_d)

# set集合的元素不会重复
set_d.add(6)
print(set_d)
