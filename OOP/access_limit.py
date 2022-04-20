# 访问限制
class Person():
    def __init__(self, name, age):
        self.name = name
        # age参数私有化
        self.__age = age

    def introduce_self(self):
        print(self.name, self.__age)

    # 方法私有化
    def __introduce_self2(self):
        print(self.name, self.__age)

    # 定义修改年龄的方法
    def set_age(self, age):
        if age <= 0 or age >= 170:
            raise Exception("非法入参,年龄不合法")
        self.__age = age


person = Person("tomcat", 12)

# 非法入参生效
# person.age = -1
# 对age参数私有化使得person.age = -1的操作不能成功


# 两个_表示方法私有化
person.set_age(10)
# 外部修改并不生效但是会新增一个 '__age': 10000}属性
person.__age = 10000

# 查看person对象的属性
# {'name': 'tomcat', '_Person__age': 10, '__age': 10000}
# 为什么实例person中还有'__age': 10000,因为pyhton是一门动态语言，实例化完成之后可以添加属性
# '_Person__age': 10实例变量__age以_Person__age的名字保存
# __age__不再表示私有,而是表示__age__属性
print(person.__dict__)

# person.introduce_self()
# tomcat 12
person.introduce_self()

# python只是提供类似私有的语法,但是私有方法还是可以访问的,但是这种方式并不符合我们的面向对象的原则,强制的改变并不可行
print("============%d" % person._Person__age)

# 并且我们还能修改
person._Person__age = 1000
print("============%d" % person._Person__age)

#
