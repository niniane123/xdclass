print("Hello World")
# 浮点型 科学计数法
print(1.1e2)
# 用type函数判定数字的类型，python确实简洁
print(type(1.23))
# 证明数字类型不可变
a = 1
print(id(a))
a = a + 1
print(id(a))
