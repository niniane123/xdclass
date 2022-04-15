# 不知道为啥，我的_init_.py的函数没有执行
# 导入包的时候，会执行__init_ .py里的内容
# 将要导入的包全部写在_init_.py文件中,这样其他地方导入的时候只需要导入我们的test包，因为会执行init.py就可以执行相关的模块导入工作
import sys
import math
import datetime

_all_ = ["test_a", "test_b"]
print("hello world")
