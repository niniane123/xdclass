def person(name, age):
    print(name, age)


# 直接指定参数名
person(name="zhangrenchao", age=11)
# 基于位置的参数匹配逻辑——有bug
person(11, "zhangrenchao")


# 使用命名关键字的时候的参数匹配逻辑:多个参数的时候只能按照参数名去匹配，此显式的写出来有利于程序的可读性
def person2(name, *, sex):
    print(type(sex))
    print("name为:%s,sex为:%s" % (name, sex))


person2("zhangrenchao", sex="男")


# 在命名关键字参数后面给默认值
# 参数前面加上*,表示这个参数是一个按照名字匹配的参数，不能按照位置匹配
def person3(name, *, sex="male"):
    print(type(sex))
    print("name为:%s,sex为:%s" % (name, sex))


person3("niniane")

# : person3() takes 1 positional argument but 2 were given
# person3()只接受一个位置参数，但是我们传递过来了两个位置参数"niniane"和”female“
person3("niniane", "female")
