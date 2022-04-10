# map函数
# map(fun, *iterables),将function作用到iterables上，并且作为一个新的iterablesfa返回
# iterables可以是一个也可以是多个
# map函数经常和lamda表达式结合使用

def add_one(x):
    return x + 1


# 对list中的每一个元素执行了add_one这个函数执行的操做
result_list = map(add_one, [1, 2, 3])
# <map object at 0x00000209743EFF10>
print(result_list)
print(list(result_list))

my_function = lambda x, y: x + y
print(map(my_function, [1, 2, 3], [4, 5, 6]))

print(list(map(my_function, [1, 2, 3], [4, 5, 6])))
# 当可迭代对象中元素个数不一样的时候，以少的为主
print(list(map(my_function, [1, 2, 3], [4, 5, 6, 3, 4, 5, 6, 7, 8, 9, 0])))
