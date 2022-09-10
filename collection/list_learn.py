"""

    列表可以一次性存储多个数据，且可以为不同的数据类型

    列表的常用操作：增删改查
        查找：
            下标查找:print(name_list[1])

            查找函数:
                index(数据，开始位置下标，结束位置下标)；返回指定数据所在位置的下标
                count()：统计指定数据在当前列表中出现的次数
                len():访问列表长度，即列表中的数据的个数

       判断
            判断是否存在:
                in():判断置顶数在某个列表序列，如果在返回True;如果不在返回False()
                not in():判断指定数据不在某个列表序列，如果不在返回True，在就返回False()




"""
name_list = ["tom", "helen", "nancy"]
print(name_list)
print(name_list[1])

# 查找元素的操作 查找nancy 但是这玩意像是多此一举啊

name_list[name_list.index("nancy")]

# 如果元素不在list中则会报错
# ValueError: '-1' is not in list s
# name_list.index("-1")

print(len(name_list))
print("toms" not in name_list)



