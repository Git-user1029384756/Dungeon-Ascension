from character import Character
from colorama import Fore, Style
from config import VICTORIES_REQUIRED

class Player(Character):
    def __init__(self, name : str, class_type : str, max_hp : int, attack : int, defense : int):
        super().__init__(name, max_hp, attack, defense)
        self.class_type = class_type
        self.level = 1
        self.xp = 0
        self.inventory = {'Potion' : 1}
        self.current_floor = 1
        self.victories_on_floor = 0
    
    @classmethod
    def from_dict(cls, name : str, data : dict):
        player = cls(
            name= name,
            class_type = data['class_type'],
            max_hp= data['max_hp'],
            attack= data['attack'],
            defense= data['defense']
                     )
        player.level = data['level']
        player.xp = data['xp']
        player.current_hp = data['current_hp']
        player.inventory = data['inventory']
        player.current_floor = data['current_floor']
        player.victories_on_floor = data['victories_on_floor']
        return player
    
    def to_dict(self):
        return {'class_type' : self.class_type,
         'level' : self.level,
         'xp' : self.xp,
         'max_hp' : self.max_hp,
         'current_hp' : self.current_hp,
         'attack' : self.attack,
         'defense' : self.defense,
         'inventory' : self.inventory,
         'current_floor' : self.current_floor,
         'victories_on_floor' : self.victories_on_floor}
    
    def add_xp(self, amount : int):
        self.xp += amount
        while self.xp >= 100:
            self.xp -= 100
            self.level += 1
            self.max_hp += 10
            self.attack += 3
            self.defense += 1
            self.current_hp = self.max_hp
            print(Style.BRIGHT + Fore.YELLOW + 'Level Up!')

    def use_potion(self):
        if self.inventory.get('Potion', 0) < 1 :
            print('\nYou do not have any potions to heal yourself !\n')

        elif self.current_hp == self.max_hp:
            print('\nCan\'t use potion, HP is already full.\n')

        else:
            self.inventory['Potion'] -= 1
            heal_amount = self.max_hp // 2
            new_hp = min(heal_amount + self.current_hp, self.max_hp)
            print(f'\nHealed {new_hp - self.current_hp} hp.\n')

            self.current_hp = new_hp

    def _bar(self, current : int, maximum : int, length=20):
        filled = int(length * current / maximum)
        return '█' * filled + '-' * (length - filled)

    def display_stats(self):
        print('╔' + '═' * 38 + '╗')
        print(f'║ {self.name} the {self.class_type:<26} ')
        print()

        print(f'║ Level        : {self.level:<21} ')
        print(f'║ Floor        : {self.current_floor:<21} ')
        print()

        print(f'║ XP           : {f"{self.xp}/100":<21}')
        print(f'║               [{self._bar(self.xp, 100)}] ')
        print(f'║ HP           : {self.current_hp}/{self.max_hp:<18} ')
        print(f'║               [{self._bar(self.current_hp, self.max_hp)}] ')        
        print()

        print(f'║ Attack       : {self.attack:<21} ')
        print(f'║ Defense      : {self.defense:<21} ')
        print()

        print('║' + 'Inventory'.center(38, '-'))
        print(f'║ Potions      : {self.inventory.get("Potion", 0):<21} ')
        print()

        print(f'║ Victories    : {self.victories_on_floor}/{VICTORIES_REQUIRED:<19} ')
        print('╚' + '═' * 38 + '╝')