# 需求 将小于房子剩余面积的家具摆放到房子中
# 分析：房子和家具是两类事务，所以要定义两个类
class House():
    # 定义属性并且初始化： 剩余面积,家具列表，其实不应该做这种无参构造方法，应该写成带参数的构造方法，这样子更加贴合实际
    def __init__(self):
        self.left_area = 0
        self.furniture_area = 0
        self.furniture_list = []

    # 用于设置house的属性
    def set_attribute(self, left_area, furniture_area):
        self.left_area = left_area
        self.furniture_area = furniture_area

    def __str__(self):
        return f"房屋的剩余面积为{self.left_area};房屋的家具面积为{self.furniture_area}"

    # 搬家的方法 moved_furniture表示要移动的家具
    def move_furniture(self, moved_furniture):
        if self.left_area < moved_furniture.area:
            raise Exception("剩余房屋面积不足，不能搬家")
        self.furniture_area += moved_furniture.area
        self.left_area -= moved_furniture.area
        self.furniture_list.append(moved_furniture.name)


class Furniture():
    # 名字，占地面积
    def __init__(self, name, furniture_area):
        self.name = name
        self.area = furniture_area;

    def __str__(self):
        return f"家具{self.name}的占地面积为{self.area}"


chair = Furniture("chair", 20)
print(chair)
house = House()
house.set_attribute(100, 0)
house.move_furniture(chair)
print(house)
