# python 中可以喂实例属性和方法设置私有权限，即设置某个实例属性或者实例方法不继承给子类
# 设置私有权限的方法，在属性名和方法名前面加上两个下划线__

# 私有方法和私有属性不能继承给子类
class Master(object):
    def __init__(self):
        self.formula = None
        # 设置钱为私有属性不继承给子类
        self.__money = 100

    def make_cake(self):
        print(f"运用{self.formula}制作蛋__money糕")

    # 对外提供访问和修改私有属性的方法
    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    # 定义私有方法
    def __info_print(self):
        print(f"师父的钱为：{self.__money},师傅的配方为{self.formula}")


class Prentice(Master):
    def __init__(self):
        # 徒弟的
        self.money = 5000

    def info_print(self):
        print(f"money:{self.money}")


class TuSun(Prentice):
    pass


prentice = Prentice()
# 不能访问父类中的私有方法和属性
# print(prentice.__money)
# print(prentice.money)
# prentice.__info_print()

tu_sun = TuSun()
print(tu_sun.money)
# 如果是实例对象调用实例方法，实例方法中的self参数是不需要传递的，pyhton解释器能自动的得到是哪个对象再调用这个方法；也也就是说他自动的给self参数赋值
tu_sun.info_print()

# 获取和修改私有属性
# 注意：私有属性和私有方法只能在类里面访问和修改
# 约定：再python中一般定义函数名get_xx来获取私有属性，定义set_xxx来修改私有属性值；
