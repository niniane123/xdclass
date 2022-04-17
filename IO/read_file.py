# "C:\Users\Hp\Documents\hello_python.txt"
# 利用open()函数打开文件
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#     Open file and return a stream.  Raise OSError upon failure.

# mode参数详解，多种参数可以相互组合
#     'r'       open for reading (default)
#     'w'       open for writing, truncating（截短, 截断，原有的内容会被删除） the file first，打开文件只用于写入，文件存在则打开，并且从开始进行编辑
#     'x'       create a new file and open it for writing  #文件在新建之前存在，报错
#     'a'       open for writing, appending to the end of the file if it exists 如果存在向文件后面添加内容
#     'b'       binary mode 以二进制的形式打开文件
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)  打开文件用于读写
#     'U'       universal newline mode (deprecated)  已经废弃
# help(open)

# r+读取文件不存在会报错
# w+读取文件不存在会创建

file_path = "C:\\Users\Hp\\Documents\\hello_python.txt"
file = open(file_path, "r", encoding="utf-8")
# 读取文件的第一行
content = file.readline()
try:
    file = open(file_path, "r", encoding="utf-8")
    # 读取文件的第一行
    # content = file.readline()
    # print(content)

    # 读取文件中所有的内容,一次性读取全部，会导致内存溢出，一般我们都放在循环中顺序读取
    # all_content = file.read()
    # print(all_content)

    print("===============")
    # readlines()读取多行封装成list
    lines = file.readlines()
    print(type(lines))
    print(len(lines))
    for line in lines:  # 依次读取每行
        line = line.strip()  # 去掉每行头尾空白
        print("读取的数据为: %s" % (line))


finally:
    file.close()

# 不用try-finally,读取完成自动关闭资源
print("=====================")
with open(file_path, "r", encoding="utf-8") as file:
    print(file.readline())
    print(file.read())
