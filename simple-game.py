import random

class game:
    life = 400
    def __init__(self, name):
        self.name = name
    def defense(self, action):
        if action == 1:
            print(f"{self.name}使用格檔 ! 將攻擊傷害減半")
            return 0.5
        elif action == 2:
            print(f"{self.name}嘗試閃避攻擊")
            dice = random.choice([0.2, 1])
            if dice == 1:
                print("閃避失敗 :( ")
            else :
                print("成功躲避攻擊 :) ")
            return dice
        
class soldier(game):
    def  attack(self, action):
        if action == 1:
            print(f"{self.name}突刺攻擊!")
            return 200
        elif action == 2:
            print(f"{self.name}星爆氣流流斬!!")
            trick = random.choice([300, 100])
            if trick == 100:
                print("絕招失敗-.-")
            else:
                print("成功施放給予致命一擊 =W=")
            return trick
            
        
class boss(game):
    def  attack(self, action):
        if action == 1:
            print(f"{self.name}爪擊!")
            return 200
        elif action == 2:
            print(f"{self.name}腐蝕毒液!!")
            trick =  random.choice([300, 100])
        if trick == 100:
            print("魔王失誤 (>-<)")
        else:
            print("給予你致命的一擊")
        return trick
        
 
player_name = input("請輸入姓名:")
player = soldier(player_name)
enemy = boss("魔王")
pc = random.choice([1, 2])
while True:
    attack_action = int(input("選擇攻擊方式\n(1)普通攻擊\n(2)特殊攻擊 :"))
    attack_power = player.attack(attack_action)
    lose_blood = int(enemy.defense(pc)*attack_power)
    enemy.life -= lose_blood
    
    if enemy.life <= 0:
        print(f"{enemy.name}陣亡，{player.name}勝利!!")
        break
    else:
        print(f"{enemy.name}受到了{lose_blood}傷害!生命剩下{enemy.life}")
        print("")
    
    defense_action = int(input("選擇防禦方式\n(1)格檔\n(2)閃避 :"))
    boss_attack = enemy.attack(pc)
    lose_blood = int(player.defense(defense_action) * boss_attack)
    player.life -= lose_blood
    if player.life <= 0:
        print(f"{player.name}受重傷倒下，遊戲結束")
        break
    else:
        print(f"{player.name}受到了{lose_blood}傷害!生命剩下{player.life}")
        print("")