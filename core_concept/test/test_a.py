a = 12

# this is core_concept 下的hello world
# hello module test
from core_concept.module_test import *

print(test_c.a)
import sys


def curent_function():
    # 如果执行的程序是当前我们指定的模块，那么__name__就是main__main__
    if __name__ == "_main_":
        print("this is _main_")
    else:
        # 如果不是，输出具体名字
        print("current module is ：" + __name__)

# curent_function()
