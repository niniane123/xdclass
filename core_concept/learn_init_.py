# _init_.py的学习
# #标志所在目录是一个模块包
# 本身也是一模块
# 可用无定义模糊导入的时候要导入的内容
# 导入包的时候，会执行__init_ .py里的内容
# 可用于批量导入模块

# 课后习题:如果我想一次性导入一个包中所有的模块，怎么办?能否使用* ?


# 导入模块
# import core_concept.module_test.test_c as test_c
# import core_concept.module_test.test_d as test_d
from core_concept.module_test import *

# 导入包
# import test
# 注意是两个下划线，我就说怎么不对呢
print(test_c.a)
print(test_d.b)
