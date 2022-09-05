# 类属性和实例属性
# 设置和访问类属性·
# 类属性就是类对象所拥有的属性，他被该类的所有实例对象用用
# 类属性可以使用类对象或者实例对象访问

# 类属性的优点
# 记录的某项数据始终保持一致的时候则定义类属性
#  实例属性要求没有给对象为其内存单独开辟一份内存空间来记录数据，而类属性为全类公寓，仅占用一份内存，更加的节省空间
class Dog(object):
    # 设置Dog的类属性  Java中这种像是实例属性哈哈，但是再python中这是类属性
    tooth = 10


wangcai = Dog()
xiaohei = Dog()
# 说明这个类属性是全体对象共有的独一份数据
# 1804226462224
print(id(wangcai.tooth))
# 1804226462224
print(id(wangcai.tooth))
# 1804226462224
print(id(wangcai.tooth))

#########################修改类属性########################################################
# 类属性只能通过类对象修改，不能通过实例对象修改，如果通过实例对象修改类属性，表示的是创建了一个和类属性同名的实例属性
# 验证修改类属性 通过类对象来修改
Dog.tooth = 100
print(wangcai.tooth)
print(xiaohei.tooth)

# 验证通过实例对象去修改类属性 通过实例对象来修改
# 这边其实是再wangcai对象中创建了一个同名叫做tooth的实例属性
wangcai.tooth = 5000
print(wangcai.tooth)
# 说明Dog的类属性没有被修改成功
print(xiaohei.tooth)
print(Dog.tooth)
