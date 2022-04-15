# 设计模式之装饰器模式
# 允许向现有类型添加新的功能，而不改变原来功能的结构
import time


# 代码缺陷：修改了原来的函数，有风险
def my_fun():
    # 统计函数执行花费时间
    start_time = time.time()  # 取系统的时间戳
    print("this is a function")
    time.sleep(3)
    end_time = time.time()
    print("函数执行时间为：%s" % (end_time - start_time))


# 使用装饰器模式去优化代码
def my_fun2():
    print("this is my  function two")


def execute_time(func):
    start_time = time.time()
    func()
    time.sleep(3)
    end_time = time.time()
    print("函数执行时间为：%s" % (end_time - start_time))


# 执行my_fun2并且统计执行时间。缺点，还是有修改，要执行execute_time的操作()
# execute_time(my_fun2)


# 进一步优化：直接调用my_fun2来实现统计时间的功能
def print_cost(func):
    def wrapper():
        start_time = time.time()
        func()
        time.sleep(3)
        end_time = time.time()
        print("函数执行时间为：%s" % (end_time - start_time))

    return wrapper


@print_cost
def my_fun3():
    print("this is my function three")


my_fun3()
