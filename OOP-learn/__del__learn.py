# 当删除对象的时候python解释器也会默认调用__del__()方法

class Washer():
    def __init__(self, width: object, height: object) -> object:
        self.width = width
        self.height = height

    def __del__(self):
        print(f"对象{self}已经被删除")


washer = Washer(10, 20)

# 对象<__main__.Washer object at 0x0000019093A6FFD0>已经被删除
