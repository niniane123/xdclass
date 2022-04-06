# if 条件->处理
# else 处理
# elif 条件1——>处理1
# elif 条件2->处理2
a = 1
b = 1
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print("a等于b:%s" % b)

# 三元表达式 if 条件判断 else 条件为假
# 条件为真的结果 if 条件判断 else 条件为假的结果
a = 2
b = 1
# 代码更加简洁
print(a if a > b else b)
print(b if a == b else a)
