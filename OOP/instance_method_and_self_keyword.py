# 面向对象中的实例方法和self关键字

# 实例方法：必须要有self入参，表示和具体的实例对象绑定，并且一般通过实例对象调用，而非类名调用

# 类方法和静态方法
class Person():
    total = 0

    def __init__(self):
        pass

    @classmethod
    # 定的类方法参数名为cls,用于操作类变量
    def print_total(cls):
        cls.total += 1
        print(cls.total)


# 类方法调用,推荐使用类名调用，不要使用具体的实例调用（虽然也可以这样做）
Person.print_total()


# 静态方法，仅仅是托管于类下面， 与类本身和类的任何实例没有任何的关系
# 静态方法不能使用类或者实例的任何属性
class Person2():
    @staticmethod
    def print_hello():
        print("Hello World")


# 静态方法的调用
Person2.print_hello()

# 总结
# 实例方法，与具体的实例相关，用于操作实例变量
# 类方法，与类相关，用于操作类变量，虽然实例可以直接调用，但是不建议通过实例调用
# 静态方法：与类和具体的实例无关，相当于一个独立函数
