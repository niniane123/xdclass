# 列表生成

# 简单的列表生成
print(list(range(10)))

# 列表生成式 expr for iter_var in iterable  对在iterable中的iter_var对象执行express的操作
# 列表生成式 expr for iter_var in iterable if condition_expression  只有满足condition才可以
# 只有满足condition才能对在iterable中的iter_var对象执行express的操作


list_a = [ele * 2 for ele in range(10, 100)]
print(list_a)
list_b = list(ele + 20 for ele in range(10, 10000))
print("this is list b:" + list_b.__str__())

# 100以内所有偶数的列表
list_c = list(ele for ele in range(101) if ele % 2 == 0)
print("this is list c:" + list_c.__str__())

list_d = [[mem, elem] for mem in range(0, 10) for elem in range(0, 20)]
print("this is list d:" + list_d.__str__())



