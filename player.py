from item import Consumable
from character import Character
from inventory import Inventory
from colorama import Fore, Style
from item import Equipment, item_from_dict
from config import VICTORIES_REQUIRED, RARITY_COLORS

class Player(Character):
    def __init__(self, name : str, class_type : str, max_hp : int, attack : int, defense : int):
        super().__init__(name, max_hp, attack, defense)
        self._base_max_hp = max_hp
        self._base_attack = attack
        self._base_defense = defense
        self.class_type = class_type
        self.level = 1
        self.xp = 0
        self.inventory = Inventory()
        self.equipment = {
            'weapon' : None,
            'armor' : None
        }
        self.current_floor = 1
        self.victories_on_floor = 0
    
    @property
    def max_hp(self):
        total = self._base_max_hp
        for item in self.equipment.values():
            if item:
                total += item.modifiers.get('max_hp', 0)
        return total
    
    @max_hp.setter
    def max_hp(self, value):
        self._base_max_hp = value
    
    @property
    def attack(self):
        total = self._base_attack
        for item in self.equipment.values():
            if item:
                total += item.modifiers.get('attack', 0)
        return total
    
    @attack.setter
    def attack(self, value):
        self._base_attack = value
    
    @property
    def defense(self):
        total = self._base_defense
        for item in self.equipment.values():
            if item:
                total += item.modifiers.get('defense', 0)
        return total
    
    @defense.setter
    def defense(self, value):
        self._base_defense = value

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
        player.inventory = Inventory.from_list(data_list= data.get('inventory', []))
        saved_equipment = data.get("equipment", {})
        for slot in player.equipment:
            saved_item = saved_equipment.get(slot)
            player.equipment[slot] = item_from_dict(item= saved_item) if saved_item is not None else None
        player.current_floor = data['current_floor']
        player.victories_on_floor = data['victories_on_floor']
        return player
    
    def to_dict(self):
        return {'class_type' : self.class_type,
         'level' : self.level,
         'xp' : self.xp,
         'max_hp' : self._base_max_hp,
         'current_hp' : self.current_hp,
         'attack' : self._base_attack,
         'defense' : self._base_defense,
         'inventory' : self.inventory.to_list(),
         'current_floor' : self.current_floor,
         'victories_on_floor' : self.victories_on_floor,
         'equipment' : {
             slot : item.to_dict() if item else None
             for slot, item in self.equipment.items()
         }}
    
    def get_equipable_items(self):
        return [item for item in self.inventory.items if isinstance(item, Equipment)]
    
    def equip_item_by_name(self, name : str):
        for item in self.inventory.items:
            if isinstance(item, Equipment) and item.name.lower() == name.lower():
                return self.equip_item(item= item)
        else:
            return "Item not found or not equipable."
    
    def equip_item(self, item : Equipment):
        slot = item.slot

        if slot not in self.equipment:
            return 'Invalid Equipment slot'
        
        if self.equipment[slot] is not None:
            self.unequip(slot= slot)

        self.inventory.remove_item(item= item)
        self.equipment[slot] = item

        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
            
        
        return f'{RARITY_COLORS.get(item.rarity, Fore.LIGHTWHITE_EX) + item.name} equipped in {slot} slot.'

    def unequip(self, slot : str):
        if slot not in self.equipment:
            return 'Invalid slot.'
        
        item = self.equipment.get(slot)

        if item is None:
            return 'Slot already empty.'
        
        self.equipment[slot] = None
        self.inventory.add_item(item= item)

        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
        
        return f'{RARITY_COLORS.get(item.rarity, Fore.LIGHTWHITE_EX) + item.name} unequipped.'
    
    def add_xp(self, amount : int):
        self.xp += amount
        while self.xp >= 100:
            self.xp -= 100
            self.level += 1
            self._base_max_hp += 10
            self._base_attack += 3
            self._base_defense += 1
            self.current_hp = self.max_hp
            print(Style.BRIGHT + Fore.YELLOW + 'Level Up!')

    def use_item(self, template_id):
        items = self.inventory.find_all_by_template(template_id= template_id)

        if not items:
            print('Item not Found.')
            return
        
        item = items[0]
        
        if not isinstance(item, Consumable):
            print('This item cannot be used')
            return
        
        success = item.use(self)

        if success:
            print(f'You used {item.name}.')
            if item.quantity < 1:
                self.inventory.remove_item(item= item)
        else:
            print('This item has no effect.')

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

        print(f'║ Victories    : {self.victories_on_floor}/{VICTORIES_REQUIRED:<19} ')
        print('╚' + '═' * 38 + '╝')
    
    def display_inventory(self):
        print()
        for index, item in enumerate(self.inventory.items, 1):
            if isinstance(item, Equipment):
                color = RARITY_COLORS.get(item.rarity, Fore.LIGHTWHITE_EX)
                print(f'{index}- {color + item.name}')
            else:
                print(f'{index}- {Fore.LIGHTWHITE_EX + item.name}')
        print()
    
    def display_equipment(self):
        print()
        for slot, item in self.equipment.items():
            if isinstance(item, Equipment):
                color = RARITY_COLORS.get(item.rarity, Fore.LIGHTWHITE_EX)
                print(f'{slot.capitalize()} : {color + item.name if item else "Empty"}')
            else:
                print(f'{slot.capitalize()} : {Fore.LIGHTWHITE_EX + item.name if item else "Empty"}')
        print()