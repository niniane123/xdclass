# 在python中引入模块 import关键字
# 1.查找一个模块必要时加载并且初始化
# 2.在局部命名空间中为import语句发生位置所处的作用域定义一个或者多个名称
# 3.一个模块首次被导入的时候，里面的代码会被执行 hello this is test module
# 导入同一个包
# import test_moudule as tm

# print(tm.a)

# 动态导入，用的不是很多
import importlib

test_module = importlib.import_module("test_moudule")
print(test_module.a)

# 导入另外的包  from package import
from function import api_in_python as api

api.test_module()

# 一次性导入如一个包中所有的模块
from function import *

# 在python中导入模块中的变量 from 模块名 import 变量名
from test_moudule import a, b, c

# 通配符导入建议开发中少用，为了代码的可读性
from test_moudule import *

print(c)
