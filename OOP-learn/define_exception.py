# python中自定义异常学习


# 语法：raise 异常类对象

# 自定义异常类继承Exception
class ShortInputException(Exception):

    # 用于初始化异常的描述信息,就算是异常他也有基本的属性，这是面向对象的基本特征
    def __init__(self, min_len, pwd_len, ):
        self.pwd_len = pwd_len
        self.min_len = min_len

        # 定义异常的描述信息

    def __str__(self):
        return f"ShortInputException:min_len为{self.min_len},pwd_len为{self.pwd_len}"

    # 这里不应该做校验的逻辑，这个异常类只是单纯的异常定义即可，不需要任何的校验逻辑，因为
    # 不同的人校验的策略是不一样的，但是他们都可以抛出这个异常


def check_pwd_len(pwd, min_len):
    if min_len > len(pwd):
        # raise ShortInputException()这边会调用ShortInputException类的初始化方法去初始异常，异常那边的返回信息result是魔法方法__str_()返回的
        raise ShortInputException(min_len, len(pwd))


def execute():
    pwd = input("请输入密码:")
    min_len = 6
    # 校验密码长度
    try:
        check_pwd_len(pwd, min_len)
    except Exception as result:
        # 异常那边的返回信息result是魔法方法__str_()返回的
        print(f"发生异常{result},请重新输入密码!")
        # 调用本身重新输入密码 递归调用
        execute()
    else:
        print(f"密码输入完成，并且密码为{pwd}")


execute()
