# 嵌套循环
result = 0
for i in range(11):
    print("i的值为%d" % i)
    for j in range(101):
        result += j
        print(result)
else:
    print("循环执行结束，result为：%d" % result)
