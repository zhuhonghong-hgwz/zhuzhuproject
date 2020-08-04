"""
作业1：
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
"""
#####1 Start Husband##################################################

#定义一个父类MyHusband
class MyHusband:
    #定义两个Husband类的属性：身高height、体重weight
    height = 164
    weight = 116
    #定义一个实例属性：skin_color
    def __init__(self,skin_color):
        self.skin_color = skin_color

    #定义一个父类的watchtv方法
    def watchtv(self):
        print(f"喜欢看电视")

#打印父类的属性
print(f"他身高{MyHusband.height},重{MyHusband.weight},他是个小矮人,哈哈！\n")

#####1 End Husband##################################################

#####2 Start MyBaby#####################################################

#定义一个MyHusband的子类MyBaby
class MyBaby(MyHusband):
    #构造函数定义实例属性
    def __init__(self,bskin_color,name):
        # 使用super函数继承到父类的skin_color
        super().__init__(bskin_color)
        #子类MyBaby自己的属性
        self.name = name
        print(f"宝宝的名字叫：{self.name},有和爸爸一样的{bskin_color}皮肤")
    #定义子类的一个play方法
    def play(self,games):
        print(f"宝宝喜欢玩{games}")

#实例化一个baby对象，并传入两个实参
baby = MyBaby("黑","小不点")
#子类的baby对象可以调用到父类的watchtv方法
baby.watchtv()
#baby对象调用子类自己的play方法
baby.play("滑滑梯\n")

#####2 End MyBaby######################################################

#####3 Start Flowers##################################################

#定义一个父类Flowers
class Flowers:
    #定义了类的属性：smell
    smell = "香"
    # 定义了一个方法描述花绽放
    def bloom(self,month):
            print(f"现在是{month}月，花绽放啦，好美啊！！！\n")


#####3 End Flowers####################################################

#####4 Start MeiGui##################################################
#定义了Flowers的一个子类MeiGui
class MeiGui(Flowers):
    #定义子类自己的属性color
    color = "红色"
    #定义一个方法描述MeiGui是绽放还是凋零
    def fallen_bloom(self,mg_month):
        #如果传入发参数mg_month小于3或者大于8，则执行if语句下面的print语句
        if mg_month <3 or mg_month >8:
            print(f"现在是{mg_month}月，花开始凋零了，太可惜了。\n")
        #如果传入的mg_month参数大于等于3或者小于等于8，则通过super函数调用父类的bloom方法
        else:
            super().bloom(mg_month)

#实例化一个对象
meigui = MeiGui()
#打印出子类自己的属性以及继承了父类的属性
print(f"这是一朵{meigui.color}的玫瑰花，闻起来很{meigui.smell}")
#调用子类的fallen_bloom方法，并传入实际的月份
meigui.fallen_bloom(8)

#####4 End MeiGui####################################################

#####5 Start Dog##################################################
#定义一个Dog类
class Dog:
    #定义一个所有Dog类都有的属性:leg
    leg = 4
    #使用构造函数定义一个需要传参的实例属性:color
    def __init__(self,color):
        self.color = color
    #定义一个Dog类的wow方法
    def wow(self):
        print(f"它会汪汪叫")

#实例化一个对象，并为构造函数传入一个实参
dog = Dog("黑色")
#打印Dog类的属性
print(f"这是有{dog.leg}条腿的{dog.color}狗")
#调用类的方法
dog.wow()
#####5 End Dog##################################################