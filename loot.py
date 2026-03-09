import random, copy
from item_templates import ITEM_TEMPLATES
from item import Equipment, item_from_dict
from config import RARITY_MULTIPLIER, DROP_CHANCE, CONSUMABLE_DROP_WEIGHT

def generate_loot():

    if random.random() > DROP_CHANCE:
        return None
    
    catagory_chance = random.random()

    if catagory_chance < CONSUMABLE_DROP_WEIGHT:
        catagory = 'consumables'
    else:
        catagory = 'equipment'

    template_pool = ITEM_TEMPLATES.get(catagory, {})
    if not template_pool:
        return None
    
    template_id = random.choice(list(template_pool.keys()))
    template_copy = copy.deepcopy(template_pool[template_id])

    item = item_from_dict(item= template_copy)
    
    if isinstance(item, Equipment):
        multiplier = RARITY_MULTIPLIER.get(item.rarity, 1.0)
        for stat in item.modifiers:
            item.modifiers[stat] = int(item.modifiers[stat] * multiplier)

    return item