# 魔法方法__str__() ：当使用print输出对象的时候，默认打印对象的内存地址，如果类中定义了__str__()方法，那么
# 就会打印从这个方法中return的数据，即返回值；
# 感觉这些魔法方法总是在自动的调用而不是显式的被我们调用，如__init__（），__str__()相当于Java中的toString()？
class Washer():
    def __init__(self):
        pass

    def __str__(self):
        return "这是洗衣机的说明书"


washer = Washer()
# 这是洗衣机的说明书,如果不定义
print(washer)
