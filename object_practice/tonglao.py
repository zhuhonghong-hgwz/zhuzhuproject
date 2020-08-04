"""
作业2
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""
#定义一个天山童姥类 ，类名为TongLao
class TongLao:
    #属性有血量，武力值（通过传入的参数得到）
    def __init__(self,t_hp,t_power):
        self.t_hp = t_hp
        self.t_power = t_power
    #TongLao类里面有2个方法
    #see_people方法，需要传入一个name参数,
    def see_people(self,name):
    # 如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
        if name == "WYZ":
            print("师弟！！！！")
    # 如果传入“李秋水”，打印“呸，贱人”，
        elif name == "李秋水":
            print("呸，贱人")
    # 如果传入“丁春秋”，打印“叛徒！我杀了你”
        elif name == "丁春秋":
            print("叛徒！我要杀了你")
    #fight_zms方法（天山折梅手），需要传入敌人的hp，power，
    def fight_zms(self,e_hp,e_power):
    # 调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
        self.t_hp = self.t_hp/2
        self.t_power = self.t_power*10
    # 进行一回合制对打，
        self.t_hp = self.t_hp - e_power
        e_hp = e_hp - self.t_hp
    # 打完之后，比较双方血量。血多的一方获胜。
        if self.t_hp >e_hp:
            print(f"我叫天山童姥，我还有血量{self.t_hp},我赢了！")
        elif self.t_hp <e_hp:
            print(f"我是天山折梅手，我还剩血量{e_hp},我赢了！")


#实例化一个tonglao对象，并传入TongLao的血量和武力值
tonglao = TongLao(2000,200)
#实例化对象调用see_people方法，并传入name
tonglao.see_people("丁春秋")
#实例化对象调用fight_zms方法，并传入敌人的血量和武力值
tonglao.fight_zms(1000,200)
