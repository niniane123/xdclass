# 文件夹操作
import os as os

# 在编辑器怎么显示出来了
# 创建单层文件夹
# os.mkdir("test")

# 创建多层文件夹，首层文件夹必须要存在
# os.mkdir("test\\py")

# 简便的创建多层文件夹的方式mkdirs
# os.makedirs("test2\\python\\baidudownload")

# C:\Users\Hp\PycharmProjects\xdclass\IO
# 获取当前文件的位置getcwd
print(os.getcwd())

# 目录的跳转 ,跳转到上级目录
os.chdir("..")
# \C:\Users\Hp\PycharmProjects\xdclass
print(os.getcwd())


# 删除文件夹???怎么不能成功
# 这个api只能删除最底层的空的文件夹，如果不是最底层或者文件夹
# os.rmdir("test\\py")


# 删除某个文件夹并且包括他的子文件夹


# 删除文件夹中所有的文件

def my_mkdir(dir):
    files = os.listdir(dir)
    print(files)
    return files


#
# ['file_fooder.py', 'file_written.py', 'input_output.py', 'read_file.py', 'test', 'test2', '__init__.py']
# delete_file_path = "C:\\Users\\Hp\PycharmProjects\\xdclass\\IO\\test\\py"
# files = my_mkdir(delete_file_path)
# print(type(files))
# # .找到文件之后直接删会报错，因为当前程序的工作目录并不是我们的删除文件所在的目录
# # 修复：将路径切换到删除路径或者拼接文件的绝对路径
# os.chdir(delete_file_path)
# print(os.getcwd())
# # 删除文件操作
# for file in files:
#     os.remove(file)
#     print("成功删除文件:", file)
#
# # 删除空文件夹
# # 将工作目录移到上一层,注意缩进
# os.chdir("..")
# os.rmdir(delete_file_path)

# 删除多层目录及路径下的文件，使用递归的方式
#
# def remove_dir(dir):
#     # 判断是否是文件夹，如果是文件夹
#     if (os.path.isdir(dir)):
#         for file_or_dir in os.listdir(dir):
#             if

# 判断是否是文件，是直接删除
