# 测试模块:尝试调用自定义模块中的功能 导入模块并测试功能
# 导入的时候更加推荐这种比较细粒度的写法，避免无关的代码执行
#
from make_moudule import test_make_module as tmm

tmm()
