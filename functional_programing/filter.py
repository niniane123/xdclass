# filter:用于过滤清洗数据
#  filter(function or None, iterable) --> filter object
# 将iterable中的元素丢入function中得到运算返回值true、false;如果是true保留该元素，如果是false则丢弃
help(filter)


def is_even_numbers(x):
    if x % 2 == 0:
        return True
    return False


# <filter object at 0x000001D6F6E58CA0>

result = filter(is_even_numbers, [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 0])
print(result)
# [2, 4, 6, 8, 8, 0]
print(list(result))
