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


      增加数据
            append():list.append(element);如果append增加的是整个序列，那么就将整个序列添加到列表中；
            extend()：list.extend():与append不同的是。如果extend的是一个列表，他会将这个列表拆开来追加到原来的列表；如果是一个数据序列，会将数据序列拆开，然后逐一增加到我们的列表
            insert():指定位置新增数据 list.insert(index,element)

     删除数据：
        del
            del 目标
            del list[index]
        pop():删除指定下标的数据，默认删除最后一个，并且返回该数据
            list.pop(index)
        remove():移除列表中某个数据的第一个匹配项
            list.remove(element)

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

# 列表是一个可变长的数据，在列表中append数据的时候，改变的是原列表
list_append = name_list.append("this is an append element")
print(name_list)
print(list_append)

name_list.append(["tom2", "nancy2"])
print(name_list)

# ['tom', 'helen', 'nancy', 'this is an append element', ['tom2', 'nancy2'], 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', 'element_1', 'element_2', 'element_3']
name_list.extend("hello world")
name_list.extend(["element_1", "element_2", "element_3"])
print(name_list)

# insert能指定任何位置增加数据
name_list.insert(0, "firt element")
name_list.insert(-1, "this is last element")
print(name_list)

# 删除
# del name_list
print(name_list)

# pop()
popped_element = name_list.pop()
print(popped_element)

# remove()
removed_element = name_list.remove("helen")
print(f"removed element is {removed_element}")

# clear()表示清空列表 最终保留的就是一个空列表，里面的数据元素都被删了
name_list.clear()
print(name_list)
