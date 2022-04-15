# 不知道为啥，我的_init_.py的函数没有执行
# 导入包的时候，会执行__init_ .py里的内容
# 将要导入的包全部写在_init_.py文件中,这样其他地方导入的时候只需要导入我们的test包，因为会执行init.py就可以执行相关的模块导入工作
import sys
import math
import datetime

# 是一个list,放在_init_.py中可以标志模糊导入的模块
# 放在普通模块下，标识一个模块中那些属性允许被大搜如到其他模块中
__all__ = ["test_a", "test_b"]

# 导包的时候执行__init_ .py里的内容
print("this is core_concept 下的hello world")

# _name_ :显示当前模块在程序执行过程中的名称，如果程序的模块是当前模块则name叫做main
# 否则：是模块的名称
