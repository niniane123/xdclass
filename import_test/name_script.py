def myFunction():
    print('变量 __name__ 的值是 ' + __name__)


def main():
    myFunction()


    # if __name__ == '__main__':


# import nameScript as ns
# ns.myFunction()
main()

# 测试代码
if __name__ == "main":
    print("this is a test demo when we import module")
