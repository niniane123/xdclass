# 闭包
# 万物都对象，函数也是，那么我们的函数的返回值能否是一个函数呢


def my_power():
    n = 2

    def power(x):
        return x ** n

    return power


# <class 'function'>
print(type(my_power()))

# 16
# 得到power函数
power = my_power()
print(power(4))

# 闭包演示
# 指定n的值求x ** n：n=3,x=4，answer=16计算值为16，说明我们实际的n值为2，这就是闭包
n = 3
print(power(4))

# 原因解释：闭包：返回函数的同时将函数携带的环境一起返回
# 闭包会将环境打印出来 (<cell at 0x000001971118FFD0: int object at 0x0000019710E00110>,)
print(power.__closure__)


def my_power2():
    n = 2

    def power(x):
        nonlocal n
        n += 1
        return x ** n

    return power


my_power2_func = my_power2()
# 27 3的3次方
print(my_power2_func(3))
# (<cell at 0x00000187EA8DF640: int object at 0x00000187EA150130>,)
print(my_power2_func.__closure__)


def my_power3():
    n = 2
    fun_list = []

    for i in range(1, 3):
        # 注意，我们这里定义的power函数并没有直接传参为i,
        # 当变量是不确定的时候，闭包函数在执行的时候只会记住最外面的一个值——即我们的环境只能支持记忆最外面的值
        def power():
            return i ** n

        fun_list.append(power)

    return fun_list


func_list = list(my_power3())
# 2
print(len(func_list))

print(func_list[0]())  # 4

# (<cell at 0x000002697168F670: int object at 0x0000026971300110>, <cell at 0x000002697168F790: int object at 0x0000026971300110>)
print(func_list[0].__closure__)
print(func_list[0].__closure__[0].cell_contents)  # 2
print(func_list[0].__closure__[1].cell_contents)  # 2

print(func_list[1]())  # 4
print(func_list[1].__closure__)
# 原因：当循环结束之后i的值为2
print(func_list[1].__closure__[0].cell_contents)  # 2
print(func_list[1].__closure__[1].cell_contents)  # 2
