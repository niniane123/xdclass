# def 函数名（入参 ）
#     业务逻辑
#     return
import math


# 定义一个函数求解圆的面积
def calculate_area(radio):
    area = math.pi * radio ** 2
    return area


print(calculate_area(4))


