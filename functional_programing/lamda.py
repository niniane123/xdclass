# lamda 一般用于创建一些临时性的操作，不推荐创建过于复杂的表达式。
# 赋值操作
power = lambda x: x ** 2
print(power(3))
print((lambda x: x ** 6)(3))

power2 = lambda x, y: x ** y

print(power2(12, 324))


def add(step=1, num_list=[]):
    return [x + step for x in num_list]


def another_add_way(func, num_list=[]):
    return [(func(x) for x in num_list)]


print(another_add_way(lambda x: x + 1, [1, 2, 3, 4, 5, 6, 7]))
print(another_add_way(lambda x: x + 2, [1, 2, 3, 4, 5, 6, 7]))


def add2(lam, num_list=[]):
    print(add(num_list=[1, 2, 3, 4]))
