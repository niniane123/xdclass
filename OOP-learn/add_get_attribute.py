# 属性即特征，比如洗衣机的高度、宽度、重量等等，不同的对象里面的属性从现实意义来讲是不一样额
# 对象属性既可以在类外面添加和获取，也能在类里面添加和获取；

# 1.类外面添加对象属性  对象名.属性名=值；这样子太烂了，我们仍然参考Java的规范比较合适
class Washser():
    def wash(self):
        print("正在洗衣服")

    def print_info(self):
        # 在类中获取属性  self.属性
        print(f"宽度为{self.width}")
        print(f"高度为{self.height}")


# 在类的外部添加属性，我个人非常不推荐这种方式；
washer = Washser()
washer.width = 100
washer.height = 20

# 在类的外面获取对象属性  语法：对象名.属性名
print(f"washer的宽度是{washer.width}")
print(f"wahse的高度为是{washer.height}")

# 在类里面获取对象属性 self.属性名
washer.print_info()
