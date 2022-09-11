import name_script as ns

# 注意事项：我们在导入包的时候被导入包中的代码会全部一一执行，导致一些函数在导包的这个动作中就被执行了，要想避免这个问题我们就需要使用
# __na·me__属性去控制，
# if __name__ == "main":
ns.myFunction()
