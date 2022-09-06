# 异常的学习
# try:
# 可能发生错误的代码
# except:
# 如果出现异常要执行的代码

# 尝试以r模式打开文件，如果文件不存在，则以w的方式打开
# try:
#     text_io = open("test.txt", "r")
#     print("已经打开文件")
# except 异常类型:
#     print("发生错误，开始尝试以写的方式打开文件")
#     text_io = open("test.txt", "w")
# try:
#     print(num)
# except NameError:
#     print("发生异常了")


# try:
#     print(1 / 0)
# except (NameError, ZeroDivisionError) as result:
#     print(f"发生错误{result}")

# try:
#     print(1 / 0)
# except Exception as result:
#     print(f"发生错误{result}")

try:
    text_io = open("test.txt", "r")
# 捕获异常之后要执行的代码
except Exception as result:
    print(f"发生错误{result}")
# 不发生异常的时候要执行的代码
else:
    print("我是else，是没有异常的时候执行的代码")
finally:
    text_io.close()
    print("关闭文件io")
