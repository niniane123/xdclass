# range()
a = range(0, 5)
print(type(a))
# range(0, 5)
print(a)

# range()函数的具体用法  range(start,stop,step)  start:默认为0; step:步长 默认为1,当然也可以为-1  ：stop:无默认值，必须要指定好，生成的range序列不包括stop
# 这是一个开区间，指定start,stop,step
b = range(1, 10, 2)
# [1, 3, 5, 7, 9]
print(list(b))

# 指定 start和stop的位置
c = range(1, 6)
print(list(c))

# 必须要指定stop的位置，
print(list(range(10)))
