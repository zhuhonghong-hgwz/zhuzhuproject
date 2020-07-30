"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""

#定义一个fight函数
def fight():

        #定义四个变量并赋初值,用于存放我的和你的血量、攻击力
        my_hp = 1000
        my_power = 200
        your_hp = 1000
        your_power = 199

        #只要没有人血量为0就继续进行循环
        while True:
             #每循环一次血量就会减少，我的血量等于我剩余血量减去你的攻击力
            my_hp = my_hp - your_power
             # 每循环一次血量就会减少，你的血量等于剩余血量减去我的攻击力
            your_hp = your_hp -my_power
             #如果我的血量先为0就执行下面的print信息，并跳出while循环
            if (my_hp <= 0):
                print("我的剩余血量是：", my_hp)
                print("你的剩余血量是：", your_hp)
                print("我输了")
                break
            # 如果你的血量先为0就执行下面的print信息，并跳出while循环
            elif (your_hp <= 0):
                print("我的剩余血量是：", my_hp)
                print("你的剩余血量是：", your_hp)
                print("你输了")
                break


 #调用fight函数
fight()