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
   
   lstrip()删除左侧空白字符串
   
   rstrip()删除右侧的空白字符串
   
   strip()删除空白字符串
   
   字符串对齐：
        ljust() 方法的基本格式如下：
        S.ljust(width[, fillchar])
        
        其中各个参数的含义如下：
        S：表示要进行填充的字符串；
        width：表示包括 S 本身长度在内，字符串要占的总长度；
        fillchar：作为可选参数，用来指定填充字符串时所用的字符，默认情况使用空格。

    
        Python rjust()方法
            rjust() 和 ljust() 方法类似，唯一的不同在于，rjust() 方法是向字符串的左侧填充指定字符，从而达到右对齐文本的目的。
            rjust() 方法的基本格式如下：
            S.rjust(width, fillchar])
        
        Python center()方法
            center() 字符串方法与 ljust() 和 rjust() 的用法类似，但它让文本居中，而不是左对齐或右对齐。
            center() 方法的基本格式如下：
            S.center(width[, fillchar])
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

"""
    判断操作:
        所谓判断即为判断真假，返回的结果为布尔类型True或者False
         startswith()
            子串.startswith(子串，开始位置下标，结束位置下标)
            如果不指定开始位置下标和结束位置下标，那么就是指代的整个字符串
            
        endswith()
            endswith() 方法用于检索字符串是否以指定字符串结尾，如果是则返回 True；反之则返回 False。该方法的语法格式如下：
            str.endswith(sub,start,end)
            str：表示原字符串；
            sub：表示要检索的字符串；
            start：指定检索开始时的起始位置索引（字符串第一个字符对应的索引值为 0），如果不指定，默认从头开始检索。
            end：指定检索的结束位置索引，如果不指定，默认一直检索到结束。

        isalpha():
            如果字符串中至少有一个字符并且所有的字符都是字母则返回True;否则返回False
        
        isalnum():
            表示字符串是否是数字和字母的组合
        
        isspace():
            
            
                
        
"""
print(my_str.startswith("hello"))
# False
print(my_str.isalpha())

# False
print(my_str.isdigit())

digit_str = "123"
print(digit_str.isdigit())
# False
print(my_str.isalnum())

my_str3=""
print(my_str3.isspace())