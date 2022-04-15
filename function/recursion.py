# 递归  自己调用自己
# 递归的调用到最深层，然后从最深层返回

def calculate_factorial(n):
    if n == 1:
        return 1
    else:
        # return关键字必须要加，否则递归返回的过程不能执行
        return n * calculate_factorial(n - 1)


# 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
print(calculate_factorial(100))


# 斐波那契数列的练习
def fibonacci_calculation(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fibonacci_calculation(n - 1) + fibonacci_calculation(n - 2)


print(fibonacci_calculation(3))


def module_test():
    print("this is recursion in function package")
