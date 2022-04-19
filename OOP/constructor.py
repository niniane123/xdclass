# 构造函数，在创建对象的时候初始化对象

# Java中有多个构造函数，但是python中只有一个构造函数，并且是显式存在的

class Person():
    # 构造函数固定写法__init__
    def __init__(self):
        print("Hello Person")


class Person2():
    # 可以什么都不写，python会自动帮我们创建一个空的__init__()函数
    pass


class Person3():
    # 自带self属性，在__init__()里面定义属性并且赋值，类相关的属性都放在__init__里面和Java不相同
    # 另外我们也可以赋默认值，并不建议这么使用，在定义构造函数的时候尽量少去定义参数的默认值
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def introduce_self(self):
        print("my name is %s,and my age is %d,and my Height is %d" % (self.name, self.age, self.height))


# Hello Person
# 实例化对象的时候会调用构造函数的东西完成对象的初始化
# 同一个类构造处的对象是不相同的，包括属性的值
person = Person()

person3 = Person3(name="tomcat", age=18, height=173)
person3.introduce_self()
