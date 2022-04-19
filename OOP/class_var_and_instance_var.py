# 类变量和实例变量
# 类变量：定义再类中并且在函数体之外。类变量通常不作为实例变量使用，类变量在整个实例化的对象中是公用的
# 实例变量：定义在方法中，用self绑定在实例上，只作用于当前实例的变量

class Person():
    # 类变量：定义再类中并且在函数体之外。类变量通常不作为实例变量使用，类变量在整个实例化的对象中是公用的
    # 类变量相当于Java中的静态变量  static关键字
    age = 0

    # 实例变量：定义在方法中，用self绑定在实例上，只作用于当前实例的变量
    # name实例变量相当于Java中的成员变量
    def __init__(self, name):
        # 实例化一次age+1
        self.__class__.age += 1

        # Person.age+=1

        # 用self绑定在实例上，值作用于当前实例
        self.name = name

        self.age = 0

    def introduce_self(self):
        print("introduce my self: my name is %s,and my age is %d" % (self.name, self.age))


# 新建对象并将属性初始化
person_one = Person("tomcat")
person_one.introduce_self()
print(person_one.name)
print(person_one.age)
print(Person.age)
print(id(person_one.age) == id(Person.age))

print("=====================")
person_two = Person("zhangsan")
# False
print(id(person_one) == id(person_two))
# 类变量的访问,相当于Java中的static关键字
print(Person.age)

#
