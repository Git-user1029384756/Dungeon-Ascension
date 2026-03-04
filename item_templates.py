ITEM_TEMPLATES = {

    'consumables' : {
        'health_potion_percent' : {
            'type' : 'Consumable',
            'template_id' : 'health_potion_percent',
            'name' : 'Major Health Potion',
            'effect_type' : 'heal_percent',
            'value' : 50,
            'quantity' : 1
        },
        'health_potion_flat' : {
            'type' : 'Consumable',
            'template_id' : 'health_potion_flat',
            'name' : 'Minor Health Potion',
            'effect_type' : 'heal_flat',
            'value' : 40,
            'quantity' : 1
        }
    },

    'equipment' : {
        'rusty_sword' : {
            'type' : 'Equipment',
            'template_id' : 'rusty_sword',
            'name' : 'Rusty Sword',
            'slot' : 'weapon',
            'rarity' : 'common',
            'modifiers' : {
                'attack' : 3
            }
        },
        'bronze_sword' : {
            'type' : 'Equipment',
            'template_id' : 'bronze_sword',
            'name' : 'Bronze Sword',
            'slot' : 'weapon',
            'rarity' : 'uncommon',
            'modifiers' : {
                'attack' : 5
            }
        },
        'leather_armor' : {
            'type' : 'Equipment',
            'template_id' : 'leather_armor',
            'name' : 'Leather Armor',
            'slot' : 'armor',
            'rarity' : 'common',
            'modifiers' : {
                'defense' : 2
            }
        },
        'chainmail_armor' : {
            'type' : 'Equipment',
            'template_id' : 'chainmail_armor',
            'name' : 'Chainmail Armor',
            'slot' : 'armor',
            'rarity' : 'uncommon',
            'modifiers' : {
                'max_hp' : 10,
                'defense' : 1
            }
        }
    }
}