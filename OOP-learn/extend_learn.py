# 继承相关的知识

# 单继承
# 多继承
# 子类重写父类的同名属性和方法
# 子类调用父类的同名属性和方法
# 多层继承
# super()
# 私有属性和私有方法

# 继承的好处：1.减少代码量


# 由不同python解释器引发出两种类：经典类和新式类 在3.0版本我们是按照新式类去解释的

# 经典类
# class 类名:
#    代码


# 新式类 ：工作中都是些的新式类，()填充的是要继承的父类，不写默认继承object;
# class 类名(object):
#   代码


# python面向对象的继承指的是多个类之间的所属关系，即子类默认继承父类中的所有属性和方法，具体如下
# 单继承  class 类名（extended_object）:
# pass


# 多继承：一个类同时继承了多个父类

class Master(object):
    def __init__(self):
        self.formula = "[师父的煎饼果子配方]"

    def make_cake(self):
        print(f"运用{self.formula}制作煎饼果子")


class School(object):
    def __init__(self):
        self.formula = "[学校的煎饼果子配方]"

    def make_cake(self):
        print(f"运用{self.formula}制作煎饼果子")


# 多继承 类
class Prentice(School, Master):
    pass


# 注意：当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法
prentice = Prentice()
# [学校的煎饼果子配方]
print(prentice.formula)
# 运用[学校的煎饼果子配方]制作煎饼果子
prentice.make_cake()
