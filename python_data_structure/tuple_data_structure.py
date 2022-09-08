# 元组数据类型接结构

# 数据表示(1,2,3)  注意：当tuple中只有一个元素的时候，一定要在第一个元素后面加逗号。这样才能表示这是一个元
tuple_a = (1, 2, 3, 45, 6, 7)
print(type(tuple_a))

# tuple 支持的操作：只能读取，不能修改写入
print(tuple_a.__getitem__(3))
print(tuple_a[1:3])

import python_package_learn.test_moudule

python_package_learn.test_moudule.test()
from python_package_learn import *
test_moudule.test()