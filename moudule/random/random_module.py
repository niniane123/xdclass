import random
import random as ran
import string

print(ran.randint(10, 11))

# Random.randrange ([start,] stop [,step])
# 注意：step是从start开始的步长，通过指定我们的step配合start和end我们可以确定我们的基础集合，
print(ran.randrange(10, 199, 12))

# 返回一个随机字符
print(random.choice("agfjasokfgjrqo"))

# 从多个字符中选取特定数量的字符[ 'a' , 'd' , 'b']
print(random.sample("adfsdfjwieqf", 2))
print(string.ascii_lowercase + string.digits)

# 简单实现随机验证码
# N826
print("".join(random.sample(string.digits + string.ascii_uppercase, 4)))

# 洗牌算法
str = string.ascii_lowercase
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
str_list = list(str)
print(str_list)
# random.shuffle()用于将一个列表中的元素打乱顺序，值得注意的是使用这个方法不会生成新的列表，只是将原列表的次序打乱。
ran.shuffle(str_list)
# 再次打印原列表
print(str_list)

