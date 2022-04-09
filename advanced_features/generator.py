# 列表生成器 节省内存空间,原理：一边循环一边计算的机制

# 定义(expr for iter_var in iterable)
# 定义(expr for iter_var in iterable if condition_expression)

generator = (ele + 2 for ele in range(1, 100, 3) if ele % 2 == 0)
list_a = list(generator)
print(list_a)
# 一边生成一边计算，懒加载机制
# 生成表达式是先生成再加载
for ele in generator:
    print(generator.__next__())
