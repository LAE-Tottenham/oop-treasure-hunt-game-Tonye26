import random
class Enemy():
    def __init__(self,name,damage,health):
        self.name=name
        self.damage=damage
        self.health=health
        self.accuracy=random.randint(10,100)
    def attack(self,Player):
        if opt==2:
            Player.dodge(self,Enemy)
        else:
            Player.health=Player.health-self.damage
    def death(self):
        if self.health==0:
            print(f"{self.name} has perished")