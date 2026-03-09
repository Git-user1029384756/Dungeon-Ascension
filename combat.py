from loot import generate_loot
from colorama import Fore, Style

class BattleResult:
    def __init__(self, result : str, log : list[str], loot= None, is_boss : bool = False):
        self.result = result
        self.log = log
        self.loot = loot
        self.is_boss = is_boss


def calculate_damage(attacker, defender):
    return max(attacker.attack - defender.defense, 1)


def battle(player, enemy) -> BattleResult:

    log = []
    name = enemy.name or 'Unknown Creature'

    if enemy.is_boss:
        log.append(Style.BRIGHT + Fore.MAGENTA + f'\nA terrifying presence fills the dungeon...')
        log.append(Style.BRIGHT + Fore.MAGENTA + f'{name} emerges from the shadows!\n')
    else:
        article = 'an' if name[0].lower() in 'aeiou' else 'a'
        log.append(f'\n{player.name} encounters {article} {name}!\n')

    while player.is_alive() and enemy.is_alive():

        damage_to_enemy = calculate_damage(attacker= player, defender= enemy)
        current_enemy_hp = enemy.current_hp
        enemy.take_damage(amount= damage_to_enemy)

        log.append(Fore.GREEN + f'{player.name} strikes {name} for {current_enemy_hp - enemy.current_hp} damage!')
        log.append(f'{name} HP: {enemy.current_hp}/{enemy.max_hp}\n')

        if not enemy.is_alive():

            loot = generate_loot()
            if enemy.is_boss:
                log.append(Style.BRIGHT + Fore.MAGENTA + f'{enemy.name} has been annihilated!\n')
            else:
                log.append(Fore.GREEN + f'{name} has been slain!\n')
            return BattleResult(
                result= 'win',
                log= log,
                loot= loot,
                is_boss= enemy.is_boss
            )


        damage_to_player = calculate_damage(attacker= enemy, defender= player)
        current_player_hp = player.current_hp
        player.take_damage(damage_to_player)

        log.append(Fore.RED + f'{enemy.name} hits {player.name} for {current_player_hp - player.current_hp} damage!')
        log.append(f'{player.name} HP: {player.current_hp}/{player.max_hp}\n')

        if not player.is_alive():
            log.append(Fore.RED + f'{player.name} has fallen...\n')
            return BattleResult(
                result= 'defeat',
                log= log,
                loot= None,
                is_boss= enemy.is_boss
            )


