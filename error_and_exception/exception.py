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


def my_function():
    warnings.warn("this is a warning", DeprecationWarning)


my_function()

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
with open("my_file.txt") as file:
    for line in file:
        print(line, end="")
# FileNotFoundError: [Errno 2] No such file or directory: 'my_file.txt'
