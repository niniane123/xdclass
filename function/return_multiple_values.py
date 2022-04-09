# 函数返回多个值
# 封装到list中返回
def return_multiple_values():
    list_a = [1, 2, 3, 4]
    return list_a


# 返回多个值，tuple
def return_multiple_values1():
    return 1, 23, 4


# 接收多个返回值

a, b, c = return_multiple_values1()
print(a, b, c)
result = return_multiple_values1()
for i in result:
    print(i)
