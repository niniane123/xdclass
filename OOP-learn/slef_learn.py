# self指代的是调用该函数的对象本身，也就是该类实例化之后的对象去调用函数，如果函数中
# 有self关键字的话，那么在函数中就可以有指代该对象的句柄，有利于我们的其他操作，其实这并不是必须的我认为

class Washer():
    # self对象指代调用该函数的对象本身
    def wash(self):
        print(id(self))
        print("正在洗衣服")
    # self关键字的学习


washer = Washer()
# washer对象调用wash()方法，那么这边self关键字（def wash(selfn)）指代的就是这个wahser对象；谁（哪个对象）调用了这个函数，那么self就是指代哪个对象
washer.wash()
# 验证self所指代的对象是否是和我们的washer对象是一个对象
print(id(washer))
