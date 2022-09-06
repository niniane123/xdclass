# 静态方法的特点
# 静态方法通过装饰器@staticmethod来修饰，静态方法既不需要传递类对象也不需要传递实例对象；形参没有self和cls;
# 静态方法也能够通过实例对象和类对象去访问调用

# 静态方法的使用场景
# 当方法中既不需要使用实例对象（如实例对象、实例属性）；又不需要使用类对象（如类方法、类属性、创建实例）的时候，定义静态方法
# 取消不必需要的参数传递，有利于减少不必要的内存占用和性能消耗


class Dog(object):
    @staticmethod
    def bark():
        print("dog is barking ")


dog = Dog()

dog = Dog()
# dog is barking
dog.bark()
# dog is barking
Dog.bark()
