from player import Player
import random
class enemy():
    def __init__(self,name,damage,health):
        self.name=name
        self.damage=damage
        self.health=health
        self.accuracy=random.randint(10,100)
    def attack(self,Player):
        if opt==4:
            Player.dodge(self,enemy)
        else:
            Player.health=Player.health-self.damage