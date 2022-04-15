def my_function(x, y):
    result = x / y
    return result


my_function(12, 4)

# ZeroDivisionError: division by zero
my_function(12, 0)

# 常用快捷键
# 设置断点 在行号后单击（双击取消）
# 开始debug alt+shift+f9
# F8 执行本行的代码并且会跳转到下一行
# F7 进入
# F9 只在断点和交互处停止，快速调式
# shift + f9 运行debug模式 停止在第一个断点处 f9 停止在第二个断点处
# console模式，类似于命令行的出输，可以直观的看到程序每行代码运行的效果
