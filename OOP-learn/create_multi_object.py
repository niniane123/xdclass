# 本节目标：一个类可以创建多个对象；多个对象都调用函数的时候，slef的地址是否相同
class Washer():
    def wash(self):
        print(str(id(self)) + "=============")
        print("正在洗衣服")


# 一个类可以创建多个对象，但是对象所在的内存地址不一样，这说明这些对象是不相同的对象；
washer1 = Washer()
washer2 = Washer()
print(id(washer2))
washer2.wash()

print("=======")
washer1.wash()
print(id(washer1))
