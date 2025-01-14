import random
class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.health = 100
        self.energy = 100
        self.inventory_max_weight = 50
        self.inventory = []
        # add more atributes as needed


    def add_item(self, item_instance):
        if self.calculate_inventory_size() > self.inventory_max_weight:
            self.inventory.append(item_instance)
        else:
            print("Your inventory is full...")

    def use_item(self, item_instance):
        if item_instance.type == "food":
            self.energy += 50
        elif item_instance.type == "medicine":
            self.health += 50
        # add more code here
    def dodge(self,enemy):
        a=random.randint(0,100)
        if a>enemy.accuracy:
            print("You have successfully dodged")
    
    def attack(self,Enemy,Weapon):
        Weapon.use(Weapon,Enemy)

    # add more methods as needed