import random
class Item():
    def __init__(self, name,type):
        self.name=name
        self.type=type

class Weapon(Item):
    def __init__(self, name,damage,type="Weapon"):
        super().__init__(name, type)
        self.damage=damage
    def use(self,enemy):
        enemy.health-=self.damage
        print(f"{enemy.name} has taken {self.damage} damage")

class food(Item):
    def __init__(self, name,energy,type="Food"):
        super().__init__(name, type)
        self.energy=energy
    def use(self,player):
        player.energy+=self.energy
        print(f"You have replenished {self.energy} energy")
class tool(Item):
    def __init__(self, name, type="Tool"):
        super().__init__(name, type)
        self.uses=random.randint(1,3)
    def use(self):
        if self.uses!=0:
            self.uses=self.uses-1
            print(f"{self.name} has {self.uses} left")
        elif self.uses==0:
            print(f"{self.name} is broken")


