# python中的默认参数：我们在使用默认参数的时候，一定要注意，默认是不可变的对象，即调用一次内存地址是会发生改变的
#
def power(x, n):
    return x ** n


print(power(2, 4))


# 添加参数默认值  默认参数的位置只能在最后，不然会报错
def default_power(x, n=2):
    return x ** n


print(default_power(4))
print(default_power(4, 3))


def test(a, b=1, c=1):
    return a * b * c


print(test(43))
print(test(43, 2))
# 我们要修改默认参数就显式的对默认参数做赋值操作
print(test(a=234, c=45))


# 当默认参数为list时候
# 默认参数已经完成初始化并且赋值了，随后的调用要小心，我们在使用默认参数的时候，一定要看默认参数是不是不可变的对象
def test_default_list(para_list=[]):  # list的默认值为[]
    para_list.append("name")
    print(para_list)


# 可以不传参数
test_default_list()  # ['name']
# 诡异的计算结果
# 解释：para_list指向一个特定的地址，在定义函数的时候已经固定了，调用一次就追加一次
test_default_list()  # ['name', 'name']


# 如果不加默认值就不会有问题
def test_list(para_list):
    para_list.append(" this is append part")
    return para_list


print(test_list(["this is a test"]))

print(test_list(["this is a test"]))
