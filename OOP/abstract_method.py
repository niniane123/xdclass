# 抽象方法——一般存在抽象类或者接口中的方法，交付子类来实现

# 1. 抽象类
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def activity(self):
        # 调用自身的run()以及eat()
        self.run()
        self.eat()

    # 抽象类中的方法必须要全部去实现


# 2.子类继承抽象类
class Dog(Animal):
    def eat(self):
        print("dog is eating")

    def run(self):
        print("dog is running")


class Cat(Animal):
    def eat(self):
        print("dog is eating")

    def run(self):
        print("dog is running")


dog = Dog()
dog.eat()

print("==============")
# 3.多态
# 相当于调用了自身的eat()和run,不同的子类对象调用相同的父类方法，产生不同的执行结果的情况我们就叫做多态
# 有利于增加程序的可读性可扩展性，子类中都是调用父类的activity()方法。
dog.activity()
cat = Cat()
cat.activity()
