# 成员和身份运算符
# 成员运算符：in /not in
a = "123"
b = "12"
print(b in a)  # ture
print(a in b)  # false

# 身份运算符 is /is not  判断两个变量引用的对象是否是同一个 ==判断两个变量的值是否相等
a = "123"
b = "123"
print(a is b)  # true
print(a == b)  # true

a = [2, 3, 4, 5]
b = a[:]
print(a)
print(b)
print(a is b)  # false  is表示就是，表示两者是同一个对象，对象的概念会在后面讲解
print(a == b)  # true  比较内容
