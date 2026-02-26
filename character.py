class Character:
    def __init__(self,  name: str, max_hp : int, attack : int, defense : int):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack = attack
        self.defense = defense
    
    def take_damage(self, amount : int):
        damage = amount - self.defense
        if damage < 1:
            damage = 1
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
    
    def is_alive(self):
        return self.current_hp > 0