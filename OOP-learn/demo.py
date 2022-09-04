# 需求主线  烤地瓜，被烤的时间和状态
class FirePotato():
    # 属性定义:  烤地瓜的时间、烤地瓜的状态、调料:在__init__()方法中设置属性并且赋值初始化

    def __init__(self):
        # 总共考了多少时间
        self.total_fire_time = 0
        # 这边可以改成枚举类更快；
        self.fire_status = "fresh"
        # 调料列表空
        self.condiment = []

    def __str__(self):
        return f"地瓜的烧烤时间是{self.total_fire_time},烧烤的状态是{self.fire_status},添加的调料调料是{self.condiment}"

    # 方法定义:添加调料的方法、烤地瓜的方法
    # 设置烤地瓜的方法:烤地瓜的时间以  fire_time：表示这次烤地瓜的动作要进行多少时间
    def fire(self, fire_time):
        if fire_time < 0:
            raise Exception("烤地瓜的时间参数非法，请重新输入")
        self.total_fire_time += fire_time

        # 根据总计烧烤时间来确定地瓜的状态
        if self.total_fire_time < 3:
            self.fire_status = "fresh"
        if 3 <= self.total_fire_time < 5:
            self.fire_status = "halfcooked"
        if 5 <= self.total_fire_time <= 8:
            self.fire_status = "cooked"
        if self.total_fire_time > 8:
            self.fire_status = "burnt"

    # 添加调料的方法
    def add_condiment(self, condiments):
        self.condiment.append(condiments)


potato = FirePotato()
potato.fire(10)
potato.add_condiment(["ziran", "lajiao", "salt"])
print(potato)
