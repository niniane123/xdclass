# 类方法
# 类方法的特点
# 需要用装饰器@classmethod标识其为类方法，对于类方法第一个参数必须是类对象，关于装饰器再后面的知识点了解,一般用cls作为第一个参数
# 类方法一般和类属性配合使用
# 类方法的使用场景：一般是操作私有类属性或者类属性的时候使用 类方法
# 当方法中需要使用类对象的时候（如访问私有类属性等）定义类方法

# 类属性可以使用类对象访问 也可以使用实例对象访问，也可以配合类方法来访问；同理类方法也是遵循这样的规则
class Dog(object):
    __tooth = 10

    @classmethod
    # 默认cls表示类对象  self表示实例对象
    def get_tooth(cls):
        return cls.__tooth


dog = Dog()
print(dog.get_tooth())
print(Dog.get_tooth())
