# 在python中 __xx__()的函数叫做魔法方法，指的是具有特殊功能的函数
# __init__():初始化对象,给对象赋初始值，然后我们对象再去创建的时候修改属性
# 洗衣机的宽度和高度是与生俱来的属性，可不可以在社会年国产的过程中国就赋予这些属性能？通过__init__()方法我们可以做到这一点
class Washer():
    # __init__(): 初始化对象, 给对象赋初始值，这个值也重要，但是最重要的是定义了这个类中有哪些属性，这样子才比较符合面向对象得分要求；
    # __init__()方法在创建一个对象时候默认被调用，不需要手动调用
    # __init(self)中的slef参数不需要开发者传递，python解释器会自动的把当前的对象应用传递过去；
    def __init__(self):
        self.height = 0
        self.width = 0

    def print_info(self):
        print(f"宽度为{self.width}")
        print(f"高度为{self.height}")


# 创建对象 sef
washer = Washer()
# 从外部设置对象的属性值
washer.width = 100
washer.height = 100
washer.print_info()


##########################################################################
# 一个类可以创建多个对象，如何对不同的对象设置不同的初始化属性值呢？——传擦书
class Washer2():
    # 除了self参数还添加了height、width的形参，这样子的构造方法（也叫初始化方法）更加有利于对象的初始化
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # 好像不能像Java那样有多个构造方法
    # def __init__(self):
    #     self.height = 0
    #     self.width = 100

    def print_info(self):
        print(f"Washer2的高度是{self.height}")
        print(f"Washer2的高度是{self.width}")


# 多个__init()__方法的初试化对象的时候按照
# washer_2 = Washer2()
# washer_2.print_info()

washer_3 = Washer2(1000, 2000)
washer_3.print_info()
washer_4 = Washer2(700, 800)
washer_4.print_info()
