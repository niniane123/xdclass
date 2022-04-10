from functools import reduce


# reduce函数
# 把一个function作用在sequence上,????,类似于递归，reduce函数会将上一次的计算结果运用到本次的计算中
# reduce(function, sequence=, initial=)
# reduce(function, sequence=[1, 2, 3])
# function(function(1,2),3)


# 案例：使用reduce计算列表的乘积
# func = lambda x, y: x * y
def cal(x, y):
    print("x is %d" % x)
    print("y is %d" % y)
    return x * y


print(reduce(cal, [1, 2, 3, 4]))
# 案例：指定初始值为12

print(reduce(cal, [1, 2, 3, 4], 12))
