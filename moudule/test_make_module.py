# 测试模块:尝试调用自定义模块中的功能 导入模块并测试功能
# 导入的时候更加推荐这种比较细粒度的写法，避免无关的代码执行
#
from make_moudule import test_make_module as tmm
import sys

tmm()
# 尝试找到环境变量   PYTHONPATH
# ['C:\\Users\\Hp\\PycharmProjects\\xdclass\\moudule', 'C:\\Users\\Hp\\PycharmProjects\\xdclass', 'C:\\Program Files\\JetBrains\\PyCharm 2021.1.1\\plugins\\python\\helpers\\pycharm_display', 'C:\\Users\\Hp\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 'C:\\Users\\Hp\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 'C:\\Users\\Hp\\AppData\\Local\\Programs\\Python\\Python310\\lib', 'C:\\Users\\Hp\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\Hp\\PycharmProjects\\xdclass\\venv', 'C:\\Users\\Hp\\PycharmProjects\\xdclass\\venv\\lib\\site-packages', 'C:\\Program Files\\JetBrains\\PyCharm 2021.1.1\\plugins\\python\\helpers\\pycharm_matplotlib_backend']
print(sys.path)
