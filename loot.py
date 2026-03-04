import random, copy
from config import RARITY_MULTIPLIER
from item_templates import ITEM_TEMPLATES
from item import Equipment, item_from_dict


def generate_loot():

    BASE_DROP_CHANCE = 0.4

    if random.random() > BASE_DROP_CHANCE:
        return None
    
    catagery_chance = random.random()

    if catagery_chance < .7:
        catagory = 'consumables'
    else:
        catagory = 'equipment'

    template_pool = ITEM_TEMPLATES[catagory]
    template_id = random.choice(list(template_pool.keys()))
    template_copy = copy.deepcopy(template_pool[template_id])

    item = item_from_dict(item= template_copy)
    
    if isinstance(item, Equipment):
        multiplier = RARITY_MULTIPLIER.get(item.rarity, 1.0)
        for stat in item.modifiers:
            item.modifiers[stat] = int(item.modifiers[stat] * multiplier)

    return item