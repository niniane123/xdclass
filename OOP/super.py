# super的作用以及具体的用法


class Animal:
    def __init__(self, name):
        print("在Animal中的构造方法完成初始化")
        self.name = name

    def walk(self):
        print(self.name + " is walking")

    def eat(self):
        print("animal is eating")


# 继承Animal
class Dog(Animal):
    # super的用法一：直接使用父类的类名去调用父类的方法
    def __init__(self, name):
        print("Dog开始完成初始化....")
        Animal.__init__(self, "my bubble")
        print("Dog开始完成初始化结束....")

    # 小狗中的自有方法
    def bark(self):
        print(self.name + " is barking")

    # 验证重写覆盖父类的一个方法,当子类的方法名和参数都一样的时候,才是重写父类的方法
    def eat(self):
        print("dog is eating")


# 实例化对象
# dog = Dog("tom")
# dog.walk()
# dog.bark()


class Dog2(Animal):
    def __init__(self, name):
        super(Dog2, self).__init__(name)


dog2 = Dog2("niniane")
