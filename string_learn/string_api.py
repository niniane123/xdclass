# string:三大类api查找、修改、判断
# 查找find()
# 所谓的字符串查找方法即为查找子串在字符串中的位置或者出现的次数
# find() 检测某个子串是否存在这个字符串中，如果存在返回这个子串开始位置的下标，否则返回-1
# 语法：字符串序列.find(子串，开始位置下标，结束位置下标)
# find语法：字符串序列.find(子串，开始位置下标，结束位置下标)
# 注意：开始和结束位置下标可以省略，表示在整个字符串序列中查找
my_str = "hello world and itcast and itheima and python"
# 12
print(my_str.find("and"))

# 指定开始位置下标和结束位置的下标
print(my_str.find("and", 13, 40))

# 返回值为-1表示差找不到该字符串
print(my_str.find("ands"))

"""
        index():检测某个子串是否包含在这个字符串中，如果存在返回这个子串开始的位置下标，否则报异常
"""
print("======================")
print(my_str.index("and", 12, 50))

print(my_str.index("and"))

"""
    count()函数的使用：返回子串在字符串的出现次数，
    语法：字符串序列.count(子串，开始位置下标,结束位置下标)，开始位置下标和结束位置下标可以省略，表示在整个字符串中查找；
    注意：开始和结束位置下标可以省略，表示在整个字符串序列中查找
"""
print("=======================")
print(my_str.count("and", 15, 30))
print(my_str.count("ands", 15, 30))

"""
    rfind():和find()的功能相同，但是查找方向为右侧开始
    rindex()：和index()的功能相同，但是查找方向为右侧开始
"""

# rfind() 从右往左边开始找字符串
print("============")
print(my_str.rfind("and", 12, 50))

