# password = input("输入密码")
# zhangrenchao
# print(f"输入的密码为{password}")
#
# <class 'str'>
# print(type(password))

name_str = "zhangrenchao"
# 序列名[开始位置的下标：结束位置的下标：步长]
# 默认的步长为1
# 如果不写开始，默认从0开始;如果结束位置不写默认选取到最后
# 如果不写所有，表示所有
# 如果步长为负数，表示倒序选取，从右往左选取
# 下标为-1表示最后一个数据，依次向前类推
#  1 2 3 4 5
# -5-4-3-2-1
# 如果选取方向和步长方向冲突，则无法选取数据；
print(name_str[2:4:1])
print(name_str[:3])
print(name_str[2:])
# <class 'str'>
print(type(name_str[:]))

#