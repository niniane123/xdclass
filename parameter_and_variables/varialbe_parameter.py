# 可变长参数
#
def my_fun(username_list):
    result = 0
    for i in username_list:
        result += i
    return result


# TypeError: my_fun() takes 1 positional argument but 2 were given
# my_fun(1, 3)

# TypeError: 'int' object is not iterable
# print(my_fun(1))


def my_fun2(*username_list):
    print(type(username_list))
    result = 0
    for i in username_list:
        result += i
    return result


print(my_fun2(1, 23, 4, 5, 6))
