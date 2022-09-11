# 思考如果想要存储多个数据，但是这些数据是不可修改的，怎么做？元组

""""
    元组：定义元组使用小括号，且使用逗号隔开各个数据，数据可以是不同的数据类型
    元组不支持修改：删除、修改、增加都不支持；只支持查找操作

    查找操作：
            index(),查找某个数据，如果数据存在返回对应的下标，否则报错，语法和列表、字符串的index相同

            count()统计某个数据在当前元组出现的个数

            len():统计元组中的数据个数

"""

num_tuple = (1, 2, 3)
print(type(num_tuple))

# index()
print(num_tuple.index(1))
# 数据不存在则报错
# print(num_tuple.index("aa"))

# 通过下标访问数据
print(num_tuple[0])

# count()
print(num_tuple.count(0))

# len()
print(len(num_tuple))

# 单个数据的元组写法一定要加逗号，不然不会识别为tuple类型
# num_tuple2 = (10)
# print(type(num_tuple2))


# 元组里面元素的修改：尽可能不要去修改元组


from list_learn import imported_variable

imported_variable





