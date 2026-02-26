import time
from colorama import Fore, Style

delay : float = .8

def battle(player, enemy):
    if enemy.is_boss:
        print(Style.BRIGHT + Fore.MAGENTA + f'\nA terrifying presence fills the dungeon...')
        print(Style.BRIGHT + Fore.MAGENTA + f'{enemy.name} emerges from the shadows!\n')
        time.sleep(delay * 7)
    else:
        article = 'an' if enemy.name[0].lower() in 'aeiou' else 'a'
        print(f'\n{player.name} encounters {article} {enemy.name}!\n')
        time.sleep(delay)

    while player.is_alive() and enemy.is_alive():
        damage_to_enemy = max(player.attack - enemy.defense, 1)
        enemy.take_damage(amount= player.attack)
        print(Fore.GREEN + f'{player.name} strikes {enemy.name} for {damage_to_enemy} damage!')
        print(f'{enemy.name} HP: {enemy.current_hp}/{enemy.max_hp}\n')
        time.sleep(delay)

        if not enemy.is_alive():
            if enemy.is_boss:
                print(Style.BRIGHT + Fore.MAGENTA + f'{enemy.name} has been annihilated!\n')
            else:
                print(Fore.GREEN + f'{enemy.name} has been slain!\n')
            return 'win'

        damage_to_player = max(enemy.attack - player.defense, 1)
        player.take_damage(enemy.attack)

        print(Fore.RED + f'{enemy.name} hits {player.name} for {damage_to_player} damage!')
        print(f'{player.name} HP: {player.current_hp}/{player.max_hp}\n')
        time.sleep(delay)

        if not player.is_alive():
            print(Fore.RED + f'{player.name} has fallen...\n')
            return 'defeat'
