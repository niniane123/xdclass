# python中的继承
#
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
    # 子类的构造方法会覆盖父类中的构造方法,只要子类中显示的申明了自己的构造方法,虽然方法重载的概念要求我们参数也要保持一致
    def __init__(self, name):
        self.name = name
        print("this is Dog中的__init__")

    # 小狗中的自有方法
    def bark(self):
        print(self.name + " is barking")

    # 验证重写覆盖父类的一个方法,当子类的方法名和参数都一样的时候,才是重写父类的方法
    def eat(self):
        print("dog is eating")


class Cat(Animal):
    pass


# 实例化对象
dog = Dog("tom")
dog.walk()
dog.bark()

# cat小猫 实例化
cat = Cat("Jerry")
cat.walk()
print(cat.name)

# 子类可以就要有父类所有的属性和方法,反之父类不具备子类中的东西
print(isinstance(dog, Animal))

animal = Animal("animal")
print(isinstance(animal, Dog))

# 验证方法重载
# dog is eating
dog.eat()


# 继承的总结
# 注意事项,不要为了继承而继承,面向对象的编程思想是对现实的抽象
# 例如下面的代码就是脱离我们的现实意义的
class Person(Dog):
    pass
