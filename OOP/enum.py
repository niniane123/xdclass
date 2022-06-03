# 枚举类
# 1.红色，2：黄色；3：绿色
def judge_color(color):
    if color == 1 or color == 2:
        print("司机违规")
    else:
        print("司机正常行驶中")


# 使用枚举类优化上述代码
from enum import Enum, unique


# 使用@unique确保枚举值的唯一性
@unique
class TrafficLight(Enum):
    # 枚举成员 用1表示RED，RED表示枚举名字，1表示枚举值，对枚举值的访问，类名.枚举成员名
    # 注意：枚举类中的枚举成员名字是不能相同的，但是枚举成员的值可以相同，这种写法很奇怪，我们不推荐使用。
    RED = 1
    YELLOW = 2
    GREEN = 3
    # ValueError: duplicate values found in <enum 'TrafficLight'>: BLACK -> RED
    # BLACK = 1


# <enum 'TrafficLight'>
print(type(TrafficLight.YELLOW))
# YELLOW
print(TrafficLight.YELLOW.name)
# 2
print(TrafficLight.YELLOW.value)


# 使用枚举类优化我们的判断代码
def judge_color2(color):
    if color == TrafficLight.RED or color == TrafficLight.YELLOW:
        print("司机违规")
    else:
        print("司机正常行驶中")


# 枚举值的比较,不能参使用下面的比较代码，因为类型不一样
# Flase,
# <enum 'TrafficLight'>
print(type(TrafficLight.YELLOW))
print(TrafficLight.YELLOW == 2)

# 正确的比较方式
# True
# 值与值的比较
print(TrafficLight.YELLOW.value == 2)
# 枚举成员和枚举成员的比较
print(TrafficLight.YELLOW == TrafficLight.RED)
