import math

# 1.导入模块
# 测试模块导入是否成功，调用该模块的sqrt功能
# print(math.sqrt(9))

# 2.更加细致的粒度导入模块 sqrt就是一个函数,调用的时候就不需要模块名.功能名
# from math import sqrt
# print(sqrt(10))

# 3.from 模块名 import *  从模块中导入所有的功能
from math import *

print(sqrt(10))

# as 定义别名
# import 模块名 as 别名
# 功能定义别名
# from 模块名 import  功能名 as 别名
# 模块别名的测试 定义了别名之后只能通过别名调用
import time as ti

ti.sleep(2)
print("hello world")

# 功能别名的测试
"""
    这是测试代码
"""
from time import sleep as sl

sl(5)
print("从沉睡中苏醒了~")
