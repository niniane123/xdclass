# 闭包
# 万物都对象，函数也是，那么我们的函数的返回值能否是一个函数呢
#

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

