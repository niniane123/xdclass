# and and表示与的关系，如果x为false,x and y 返回x,否则返回y的计算值
# 即返回false
a = 3
b = 4
print(a < 2 and b > 2)
print(0 and 123)
print("bool(0)的计算值为:" + bool(0).__str__())

# or 表示或关系，对于x or y 如果x是true,返回x的值，否则返回y的值；
print("1" and "c")  # 先执行bool("1") bool("c")
print(a < 2 or b > 2)
print("" or "123")

# not
a = 0
print(not a == 2)
a = 2
print(not a == 2)
print(not a)
