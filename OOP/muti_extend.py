# python中的多继承
class Father:
    def power(self):
        print("father is powerful")

    def sing(self):
        print("father is a good singer")


class Mother:
    def sing(self):
        print("mother is a good singer")

#python支持多继承，注意多继承的写法
class Me(Father, Mother):
    pass


me = Me()
# 调用父类中的方法，当继承多个父类的时候，如果父类中有相同的方法，子类会有限使用先继承的父类中的方法
me.sing()
me.power()
