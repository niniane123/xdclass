# super()调用父类的方法 本例子是对前例的优化
# 本节探究在多继承并且子类重写父类方法的情况下如何访问父类中的属性和方法，在Java中这是一件很容易办到的事情

class Master(object):
    def __init__(self):
        self.formula = "师父的煎饼果子配方"

    def make_cake(self):
        print(f"运用{self.formula}制作煎饼果子")


class School(Master):
    def __init__(self):
        self.formula = "[学校的煎饼果子配方]"

    def make_cake(self):
        print(f"运用{self.formula}制作煎饼果子")

    def super_make_cake(self):
        super(School, self).__init__()
        super(School, self).make_cake()


# 继承
class Prentice(School):
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
        # 其实只要不是通过类名去调用实例对象，那么一般都不用传self参数
        Master.__init__(self)

        # 这里写上self的目的是为了接收将来调用这个方法的对象，self就是指代调用该方法的对象本身
        # object.make_cake()
        Master.make_cake(self)

        # 使用super的方法调用父类master中的方法
        # 1.调用父类School中的super_make_cake()方法即可

    def master_super_make_cake(self):
        super(Prentice, self).super_make_cake()

        # 这只是一个形参，把当前对象传递到其方法中，self表示调用当前方法的对象本身

    def school_make_cake(self):
        # 将当前对象传递到School.__init__()方法中进行初始化操作并且赋值 一个是初始化formula,slef表示的就是当前对象的句柄
        School.__init__(self)
        School.make_cake(self)

    def school_super_make_cake(self):
        # 这边会自动初始化父类School的formula属性吗？ 这边不是要传递一个句柄吗？super(Prentice,self)自动得到一个对象，这个对象在调用的时候已经自动的传过去了?不需要我们自己在传了吗？
        # super(Prentice, self).__init__()
        # super()返回的是一个实例对象，那么__init__()方法 是能自动接收这个调用本身的对象的
        super().__init__()
        super(Prentice, self).make_cake()


# 需求 调用父类的同名方法和属性
prentice = Prentice()
# 相当于每一次调用make_cake()都要将prentice初始化一次，使得属性重新复制
prentice.master_make_cake()
prentice.school_make_cake()
prentice.make_cake()

# 直接用super关键字不行吗_当然可以? 接下来的就是探讨这个方法
# super的带参数写法 super(当前类名,self).函数()

# super的无参数写法 super() 调用其直接父类School的方法
prentice.school_super_make_cake()

# 如果想要调用Master的方法呢
prentice.master_super_make_cake()

# 总结如果是通过对象.方法名()去调用实例方法，一般不需要我们自己传递self对象，python解释器会自动的拿到当前对象解释器的句柄；
# 如果并非如此的话那么，即我们通过类名.方法名去调用实例方法，那么虽然也可以调用，但是总归那个方法是一个实例方法，那么你定要传递一个实例对象的句柄，不然python解释器是拿不到这个对象的
