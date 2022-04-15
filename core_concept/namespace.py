# 命名空间

# 命名空间是变量到对象的映射集合，一般是通过字典来实现的，主要可以分为三类：
# 1.每个函数都有着自已的命名空间，叫做局部命名空间，它记录了函数的变量，包括函数的参数和局部定义的变量。
# 2.每个模块（python文件）拥有它自己的命名空间，叫做全局命名空间，它记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量
# 3.还有就是内置命名空间，任何模块均可访问它，它存放着内置的函数和异常。


# 命名空间的查找顺序
# 局部命名空间查找->全局命名空间查找->内置命名空间查找，查找不到会报错:NameError

# 嵌套函数查找顺序
# 1.在最底层的函数的命名空间查找
# 2.在父函数的命名空间查找
# 3.模块中查找——全局命名空间
# 4.内置命名空间中查找


# 嵌套函数查找顺序demo
def my_func():
    name = "zrc"

    def fun_son():
        name = "libai"
        print(name)

    fun_son()


# libai
my_func()

# 命名空间的生命周期
# 函数被每一次调用的时候就创建一次局部命名空间，函数执行完成，局部命名空间消失
# 全局变量a
a = 1


# 因为在函数中对a进行修改，所以a变成函数里面的局部变量，他会在这个局部命名空间中查找
def my_function():
    # 表示使用全局变量a
    global a
    print(a)
    if a == 1:
        print(a)
        a = 24


my_function()


# 局部命名空间的访问 locals()  ,locals()得到的命名空间只能读
def namespace_read():
    c = 1
    b = 2

    # <class 'dict'>
    print(type(locals()))
    # 尝试对locals命名空间中的变量做修改操作
    locals()["c"] = 3
    # {'c': 1, 'b': 2} 并不生效
    print(locals())


# key:变量名，value:变量值
# {'c': 1, 'b': 2}
namespace_read()

# 全局命名空间的访问 globals()。globals()拿到的命名空间可以读写的
# {'__name__': '__main__',
# '__doc__': None,
# '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002596A818820>,
# '__spec__': None,
# '__annotations__': {},
# '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'C:\\Users\\Hp\\PycharmProjects\\xdclass\\core_concept\\namespace.py',
# '__cached__': None, 'my_func': <function my_func at 0x000002596A363F40>,
# 'a': 24, 'my_function': <function my_function at 0x000002596A87E710>,
# 'namespace_read': <function namespace_read at 0x000002596A87E950>}
# a=24
print(globals())
# 修改globals的值
globals()["a"] = 10086
# a=10086
print(globals())
# <class 'dict'>
print(type(globals()))
