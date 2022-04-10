# 排序函数 sorted
# sorted(iterable, /, *, key=None, reverse=False)
#    默认将元素按照升序排序
#     Return a new list containing all items from the iterable in ascending order.
# key function 用于指定自己的排序规则
#     A custom key function can be supplied to customize the sort order, and the
#  reverse flag用于降序排序的标志
#     reverse flag can be set to request the result in descending order.
help(sorted)
#
result = sorted([1, 3, 3, 4, 5, 6, 7, 33, 6, 7, 8, 8, 8, 8])
# <class 'list'>
print(type(result))
print(result)

# 默认升序、第一个元素排序
data = [["python", "11"], ["Java", "44"]]
print(sorted(data))

# 指定排序关键字
print(sorted(data, key=lambda item: item[1]))
