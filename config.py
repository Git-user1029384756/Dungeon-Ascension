from colorama import Fore

CLASS_STATS = {
    'warrior' : {
        'max_hp' : 120,
        'attack' : 15,
        'defense' : 10
    },
    'rogue' : {
        'max_hp' : 90,
        'attack' : 20,
        'defense' : 5
    },
    'mage' : {
        'max_hp' : 60,
        'attack' : 25,
        'defense' : 2
    }
}


ENEMY_STATS = {
    'goblin' : {
        'max_hp' : 80,
        'attack' : 13,
        'defense' : 4,
        'xp_reward' : 10
    },
    'orc' : {
        'max_hp' : 160,
        'attack' : 20,
        'defense' : 10,
        'xp_reward' : 20
    },
    'skeleton' : {
        'max_hp' : 60,
        'attack' : 25,
        'defense' : 15,
        'xp_reward' : 25
    },
    'strong orc' : {
        'max_hp' : 220,
        'attack' : 50,
        'defense' : 30,
        'xp_reward' : 50
    },
    'malakar' : {
        'display_name' : 'Malakar, Warden of the Abyss',
        'max_hp' : 1000,
        'attack' : 40,
        'defense' : 40,
        'xp_reward' : 250,
        'is_boss' : True
    },
    'kaelthar' : {
        'display_name' : 'Kaelthar the Worldbreaker',
        'max_hp' : 500,
        'attack' : 100,
        'defense' : 25,
        'xp_reward' : 250,
        'is_boss' : True
    }
}


FLOOR_ENEMIES = {
    1: ('goblin',),
    2: ('goblin', 'orc',),
    3: ('orc', 'skeleton',),
    4: ('skeleton', 'strong orc',),
    5: ('malakar', 'kaelthar',)
}


RARITY_MULTIPLIER = {
    'common': 1.0,
    'uncommon': 1.2,
    'rare': 1.5,
    'epic': 1.8,
    'legendary': 2.2
}

RARITY_COLORS = {
    'common': Fore.LIGHTWHITE_EX,
    'uncommon': Fore.LIGHTGREEN_EX,
    'rare': Fore.LIGHTCYAN_EX,
    'epic': Fore.LIGHTMAGENTA_EX,
    'legendary': Fore.YELLOW
}

VICTORIES_REQUIRED = 5
MAX_FLOOR = 5