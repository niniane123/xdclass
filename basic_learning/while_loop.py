#  while循环
# while condition:
#     do something

# 计算100以内所有数字的和
i = 1
result = 0
while i <= 100:
    result += i
    i += 1
else:
    print("i的值为%d,while循环推出" % i)
print(result)
