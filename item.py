class Item:
    def __init__(self, template_id : str, name : str, slot : str):
        self.template_id = template_id
        self.name = name
        self.slot = slot

    @classmethod
    def from_dict(cls, data : dict):
        return cls(
            template_id= data['template_id'],
            name= data['name'],
            slot= data.get('slot')
        )

    def to_dict(self):
        return {
            'template_id' : self.template_id,
            'name' : self.name,
            'slot' : self.slot,
            'type' : self.__class__.__name__
        }
    

class Equipment(Item):
    def __init__(self, template_id : str, name : str, slot : str, rarity : str, modifiers):
        super().__init__(template_id, name, slot)
        self.rarity = rarity
        self.modifiers = modifiers
    
    @classmethod
    def from_dict(cls, data : dict):
        return cls(
            template_id= data['template_id'],
            name= data['name'],
            slot= data.get('slot'),
            rarity= data.get('rarity', 'unknown'),
            modifiers= data.get('modifiers', [])
        )
    
    def to_dict(self):
        data = super().to_dict()
        data['rarity'] = self.rarity
        data['modifiers'] = self.modifiers
        return data


class Consumable(Item):
    def __init__(self, template_id, name, effect_type : str, value : int, quantity= 1, slot= None):
        super().__init__(template_id, name, slot)
        self.effect_type = effect_type
        self.value = value
        self.quantity = quantity
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            template_id= data['template_id'],
            name= data['name'],
            slot= data.get('slot'),
            effect_type= data['effect_type'],
            value= data['value'],
            quantity= data.get('quantity', 1)
        )
    
    def to_dict(self):
        data = super().to_dict()
        data['effect_type'] = self.effect_type
        data['value'] = self.value
        data['quantity'] = self.quantity
        return data
    
    def use(self, player):
        if self.quantity < 1:
            return False
        
        if player.current_hp >= player.max_hp:
                return False
        
        if self.effect_type == 'heal_percent':
            heal_amount = int(player.max_hp * (self.value / 100))
        elif self.effect_type == 'heal_flat':
            heal_amount = self.value
        else:
            return False
        
        player.current_hp = min(player.current_hp + heal_amount, player.max_hp)
        self.quantity -= 1

        return True


def item_from_dict(item : dict):
    if item.get('type') == 'Equipment':
        return Equipment.from_dict(data= item)
    elif item.get('type') == 'Consumable':
        return Consumable.from_dict(data= item)
    else:
        return Item.from_dict(data= item)