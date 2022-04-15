# 异常的捕获和处理
# 错误、异常、警告

# 异常
# ZeroDivisionError: division by zero，本质上是异常，因为是在运行的时候报错
# print(10 / 0)

# 警告 经常忽略警告
import warnings

# warn(message, category=None, stacklevel=1, source=None)
#     Issue a warning, or maybe ignore it or raise an exception.
help(warnings.warn)

# def my_function():
#     warnings.warn("this is a warning", DeprecationWarning)


# my_function()

# 异常的处理格式
# try:
#     dosomething
# except 可能发生的异常1:
#     异常之后的处理1
# except 可能发生的异常2:
#      异常之后的处理2

try:
    print(10 / 0)
except ZeroDivisionError:
    # 除数为0

    print("除数为0")
finally:
    # finally里面的代码块无论如何都会执行
    # 执行结束
    print("执行结束")


# 预定义处理来处理异常
# 在open()的时候无论发生怎样的错误异常，都会关闭我们的IO链接
# with open("my_file.txt") as file:
#     for line in file:
#         print(line, end="")


# FileNotFoundError: [Errno 2] No such file or directory: 'my_file.txt'


# 使用自定义异常取自定义异常
# 类的概念
class self_define_exception(Exception):
    def __init__(self, parameter):
        error = "非法入参{0},分母不能为0".format(parameter)
        # 对Exception做初始化
        Exception.__init__(self, error)
        # 这行代码似乎不写也没有影响
        self.parameter = parameter


def my_function(x):
    if x == 0:
        # 抛出自定义异常
        # : self_define_exception.__init__() missing 1 required positional argument: 'parameter'
        # 这里的x是传给__init__() 函数做初始化的
        raise self_define_exception(x)
    else:
        print(10 / x)


my_function(2)


# my_function(0)


# 捕获异常之后再次抛出异常
def my_function():
    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("除数不能为0~")
        # 再次抛出捕获的异常
        raise


# 除数不能为0~
my_function()
