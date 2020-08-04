"""
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
"""
# 导入TongLao模块
from object_practice.tonglao import TongLao


# 定义一个XuZhu类，继承于童姥
class XuZhu(TongLao):
    # 虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
    def read(self):
        print("罪过罪过")


# 实例化一个xuzhu对象
xuzhu = XuZhu(800,100)
# 调用XuZhu类的read方法
xuzhu.read()
