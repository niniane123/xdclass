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

""""
    字符串的修改操作
    replace()
        替换作用
        语法：字符串序列.replace(旧子串,新子串，替换次数)
        替换次数：替换次数如果超过了旧子串的出现次数，表示替换所有的旧子串
        注意：替换次数如果查出子串的出现次数，则替换为该子串的出现次数
        
        理解：调用了replace之后，发现了原有字符串的数据并没有受到修改，修改之后的数据是replace函数的返回值，这说明字符串数据类型是不可变的数据类型；
        
            
    split() 
        分割作用，返回又给列表list;
        语法：字符串序列.split(分割字符，分割字符出现的次数)
        注意：分割字符出现了n次那么将来返回的数据个数为n+1个
    
    
    join()
        连接作用：join()用一个字符或者子串合并字符串，即将多个字符串合并为一个新的字符串
    语法；
        字符或者子串.join(多字符串组成的序列)
        表示用该字符或者子串来连接我们的字符序列
   
   capitalize()：将字符串第一个字符转换为大写
   注意：capitalize()函数转换之后，只字符串第一个字符大写，其他的字符全部小写 
   
   title():将字符串每个单词首字母转换成大写
   
   lower():字符串中的大写转为小写
   
   upper()：将字符串中的小写转为大写
    
   
        
"""
replaced_str = my_str.replace("and", "andsss")
print(replaced_str)
print(type(replaced_str))

split_list = my_str.split("and")
# ['hello world ', ' itcast ', ' itheima ', ' python']
# 丢失分割字符
print(split_list)
print(type(split_list))

my_str_split = my_str.split("and", 2)
# ['hello world ', ' itcast ', ' itheima and python']
print(my_str_split)

str_list = ["aa", "bb", "cc"]
print("=========")
new_str = "...".join(str_list)
print(new_str)

# 字符串首字母大写
print(my_str.capitalize())

# 每个单词首字母大小
print(my_str.title())

# 小写转大写
print(my_str.upper())

print(my_str.lower())





