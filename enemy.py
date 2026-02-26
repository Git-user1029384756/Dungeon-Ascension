from character import Character

class Enemy(Character):
    def __init__(self, name : str, max_hp : int, attack : int, defense : int, xp_reward : int, is_boss : bool = False):
        super().__init__(name, max_hp, attack, defense)
        self.xp_reward = xp_reward
        self.is_boss = is_boss