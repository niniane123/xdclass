# 退出循环与continue关键字,continue表示退出当前循环，进入下一轮的循环
result = 0
for i in range(10):
    if i % 2 == 1:
        print("i的值为%d,进入continue" % i)
        continue
    result += i
    print("result为%d" % result)
    print("result+=i的i值为%d" % i)

# break语句
for i in range(201):
    if i == 189:
        print("i的值为%d,整个循环退出" % i)
        break
    print("i的值为%d" % i)
