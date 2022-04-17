# 文件的写入
file_path = "C:\\Users\Hp\\Documents\\hello_python3.txt"
try:
    # 写入文件的时候一般都要用UTF-8
    file = open(file_path, "a", encoding="utf-8")
    file.write("this is a written file\n")
    file.write("this is a written file second line")
finally:
    file.close()
