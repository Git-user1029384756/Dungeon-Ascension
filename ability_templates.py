ABILITY_TEMPLATES = {
    'power_strike': {
        'template_id': 'power_strike',
        'name': 'Power Strike',
        'target_type': 'enemy',
        'category': 'offensive',

        'resource_cost': {
            'mana': 10
        },

        'effects': [
            {'type': 'damage', 'stat': 'attack', 'multiplier': 1.5, 'flat_bonus': 6}
        ]
    },
    'weakening_strike': {
        'template_id': 'weakening_strike',
        'name': 'Weakening Strike',
        'target_type': 'enemy',
        'category': 'offensive',

        'resource_cost': {
            'mana': 16
        },

        'effects': [
            {'type': 'damage', 'stat': 'attack', 'multiplier': 1.6, 'flat_bonus': 1},
            {'type': 'status_effect', 'effect_class': 'StatModifier', 'name': 'Weakened', 'duration': 2, 'stat': 'attack', 'amount': -5}
        ]
    },
    'quick_strike': {
        'template_id': 'quick_strike',
        'name': 'Quick Strike',
        'target_type': 'enemy',
        'category': 'offensive',

        'resource_cost': {
            'mana': 6
        },

        'effects': [
            {'type': 'damage', 'stat': 'attack', 'multiplier': .8, 'flat_bonus': 2},
            {'type': 'damage', 'stat': 'attack', 'multiplier': .7, 'flat_bonus': 1}
        ]
    },
    'poison_strike': {
        'template_id': 'poison_strike',
        'name': 'Poison Strike',
        'target_type': 'enemy',
        'category': 'offensive',

        'resource_cost' : {
            'mana': 15
        },

        'effects': [
            {'type': 'damage', 'stat': 'attack', 'multiplier': .5},
            {'type': 'status_effect', 'effect_class': 'DamageOverTime', 'name': 'Poison', 'duration': 3, 'potency': 6}
        ]
    },
    'fireball': {
        'template_id': 'fireball',
        'name': 'Fireball',
        'target_type': 'enemy',
        'category': 'offensive',

        'resource_cost': {
            'mana': 10
        },

        'effects': [
            {'type': 'damage', 'stat': 'attack', 'multiplier': 1.2, 'flat_bonus': 6},
            {'type': 'status_effect', 'effect_class': 'DamageOverTime', 'name': 'Burn', 'duration': 2, 'potency': 10, 'scaling': {'stat': 'attack', 'multiplier': .4}}
        ]
    },
    'heal_self': {
        'template_id': 'heal_self',
        'name': 'Heal',
        'target_type': 'caster',
        'category': 'support',

        'resource_cost': {
            'mana': 10
        },

        'effects': [
            {'type': 'heal', 'stat': 'attack', 'multiplier': 1.3, 'flat_bonus': 15}
        ]
    }
}