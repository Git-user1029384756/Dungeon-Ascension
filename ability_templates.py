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
            {'type': 'damage', 'stat': 'attack', 'multiplier': 1.5, 'flat_bonus': 5}
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
            {'type': 'damage', 'stat': 'attack', 'multiplier': 0.8, 'flat_bonus': 2},
            {'type': 'damage', 'stat': 'attack', 'multiplier': 0.7, 'flat_bonus': 1}
        ]
    },
    'fireball': {
        'template_id': 'fireball',
        'name': 'Fireball',
        'target_type': 'enemy',
        'category': 'offensive',

        'resource_cost': {
            'mana': 12
        },

        'effects': [
            {'type': 'damage', 'stat': 'attack', 'multiplier': 1.3, 'flat_bonus': 8}
        ]
    }
}