# _init_.py的学习
# #标志所在目录是一个模块包
# 本身也是一模块
# 可用无定义模糊导入的时候要导入的内容
# 导入包的时候，会执行__init_ .py里的内容
# 可用于批量导入模块

# 课后习题:如果我想一次性导入一个包中所有的模块，怎么办?能否使用* ?


# 导入模块
from core_concept.test import *
# 导入包
import test

# print(test_a.a)
# print(test_b.b)
