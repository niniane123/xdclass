# 本节探究在多继承并且子类重写父类方法的情况下如何访问父类中的属性和方法，在Java中国这是一件很容易办到的事情

class Master(object):
    def __init__(self):
        self.formula = "师父的煎饼果子配方"

    def make_cake(self):
        print(f"运用{self.formula}制作煎饼果子")


class School(object):
    def __init__(self):
        self.formula = "[学校的煎饼果子配方]"

    def make_cake(self):
        print(f"运用{self.formula}制作煎饼果子")


# 继承
class Prentice(School, Master):
    def __init__(self):
        self.formula = "徒弟的独创配方"

    def make_cake(self):
        self.__init__()
        print(f"徒弟使用{self.formula}的配方制作蛋糕")

    # self指向当前对象
    def master_make_cake(self):
        # 再次初始化：这里想要调用父类的同名方法和属性，所以不能使用Prentice自己的属性，我们要
        # 使用master初始话花当前对象，因为Prentice是继承了Master的，所以Master有效？
        # self就是一个形参用，习惯上用self关键字表示，表示调用该方法的对象本身，指向当前对象,便于理解
        Master.__init__(self)

        # 这里写上self的目的是为了接收将来调用这个方法的对象，self就是指代调用该方法的对象本身
        # object.make_cake()
        Master.make_cake(self)

    def school_make_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 需求 调用父类的同名方法和属性
prentice = Prentice()
# 相当于每一次调用make_cake()都要将prentice初始化一次，使得属性重新复制
prentice.master_make_cake()
prentice.school_make_cake()
prentice.make_cake()

# 直接用super关键字不行吗
