import time
# 嵌套的异常捕获语句，我们的异常传递流程是从外层的try-except传递到内层的try-except中
try:
    text_io = open("test2.txt", "r")
    while True:
        content = text_io.readline()
        # 代表剩下的内容已经没有了
        if len(content) == 0:
            break
        time.sleep(2)
        print(content)
except Exception as result:
    print(f"发生异常{result}")
finally:
    close = text_io.close()
    print(f"文件关闭f{close}")

