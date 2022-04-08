# 可以切片的对象 str 字符串 list
# 不可以切片的对象set/tuple/dic

# 切片的逻辑：start end step   start可以不写，表示从0开始到stop结束(不包括stop)；  end可以不写：表示从start到最后一个
# step不写，默认值为1
# 切片的逻辑从start开始到end结束，然后中间有step可以决定我们的步长
a = list(range(0, 10))

# 切片操作
print(a[0:3])

# 用负数表示倒数第几个元素
print(a[-3:-1])

# 从某个索引位置开始取到最后一个
print(a[2:])

# 取前五个，每两个取一个
print(a[:5:2])

# 字符串的切片
name = "this is my name"
print(name[0:7:2])
