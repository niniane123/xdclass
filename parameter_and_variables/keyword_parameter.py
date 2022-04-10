# 关键词参数可以允许传入0个或者任意个含有这个参数名的参数，关键字参数在函数内部可以转为字典
# kwargs表示key-value类型参数，可以是0个，也可以是n个，用两个**表示
def person(name, **kwargs):
    # <class 'dict'>将kwargs封装成key-value键值对，即dict类型
    print(type(kwargs))
    print(id((kwargs)))
    print(name, kwargs)


# 传键值对
person("zhangrenchao", simple_name="zrc", sex="male", pet_name="tomcat")

# 直接传字典
info = {"pet": "tomcat", "simple_name": "zrc"}

# TypeError: person() takes 1 positional argument but 2 were given
# 并不能直接传字典
# person("zhangrenchao", info)
# 需要使用关键字参数传递，两个**表示关键字参数,这种方式是值传递，并不是引用传递，不会改变我们函数外部的变量的值
# 这里是值传递
person("zhangrenchao", **info)
print(id(info))

#########################值传递和引用传递###############
# b的地址为2167178265104
# a的地址为:2167178265104
b = 10
print("b的地址为" + id(b).__str__())


def test(a):
    print("a的地址为:" + id(a).__str__())


test(b)
