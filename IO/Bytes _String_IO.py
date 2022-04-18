# string_io和bytes_io是在内存中操作文本
# 很多时候数据读取不一定是文件，也可以在内存中
# StringIO顾名思义就是在内存中读写str,string_io是操作字符串
# 要把str写入StringIO，我们需要先创建一个StringIO，然后像文件一样写入即可：
from io import StringIO

# 创建StringIO对象并且赋值
string_io = StringIO("Hello Wrold")
# 继续向内存中写入
string_io.write("\n Hello Wrold2")
#  从内存中读 取字符串
# print(string_io.readline())
#  Hello Wrold2   用write()方法写入的字符串只能用getValue()方法取值
print(string_io.getvalue())
# 关闭io资源
string_io.close()

# 简便方法 with
print("==============================")
with StringIO() as string_io:
    string_io.write("this is with string io")
    print(string_io.getvalue())

    # 查看io是否关闭
    # False
    print(string_io.closed)
# True
print(string_io.closed)

# bytes_io是操作二进制，存的读的都是二进制
# 导入BytesIO
from io import BytesIO

bytes_io = BytesIO()
# 利用encode()将字符串转化为二进制
# <editor-fold desc="bytes_io写入信息到内存中">
bytes_io.write("hello".encode("utf-8"))  # 这是一个注释
bytes_io.write("world".encode("utf-8"))
bytes_io.write("张仁超".encode("utf-8"))  # 这是一个注释
bytes_io.write("zhangsan")
# </editor-fold>

# 将二进制转化字符串
print(str(bytes_io.getvalue(), "utf-8"))

from io import BytesIO

# ctrl+f 查找
# ctrl+r替换  words表示完全匹配  matchcase表示大小写是否忽略
# ctrl+alt+l
# 注释 ctrl +/
# ctrl+alt+方向键前后定位跳转

# ctrl+w代码的快速选中 从内层向外层依次选中，连续按就是连续选中
# ctrl+shift++(-)代码的展开和压缩（注释 /import/循环体等折叠起来，方便观察代码的结构）
# ctrl+-(+)折叠部分代码块

# 复制一行ctrl+d
# 删除一行ctrl+y
# 移动一行ctrl+shift+方向键
