import time
from loot import generate_loot
from colorama import Fore, Style

delay : float = .7

def battle(player, enemy):
    if enemy.is_boss:
        print(Style.BRIGHT + Fore.MAGENTA + f'\nA terrifying presence fills the dungeon...')
        print(Style.BRIGHT + Fore.MAGENTA + f'{enemy.name} emerges from the shadows!\n')
        time.sleep(delay * 2.5)
    else:
        article = 'an' if enemy.name[0].lower() in 'aeiou' else 'a'
        print(f'\n{player.name} encounters {article} {enemy.name}!\n')
        time.sleep(delay)

    while player.is_alive() and enemy.is_alive():
        damage_to_enemy = max(player.attack - enemy.defense, 1)
        current_enemy_hp = enemy.current_hp
        enemy.take_damage(amount= damage_to_enemy)

        print(Fore.GREEN + f'{player.name} strikes {enemy.name} for {current_enemy_hp - enemy.current_hp} damage!')
        print(f'{enemy.name} HP: {enemy.current_hp}/{enemy.max_hp}\n')
        time.sleep(delay)

        if not enemy.is_alive():

            item = generate_loot()
            if item:
                player.inventory.add_item(item= item)
                print('You found ', Fore.LIGHTYELLOW_EX + item.name, '!')
            if enemy.is_boss:
                print(Style.BRIGHT + Fore.MAGENTA + f'{enemy.name} has been annihilated!\n')
            else:
                print(Fore.GREEN + f'{enemy.name} has been slain!\n')
            return 'win'
        
        damage_to_player = max(enemy.attack - player.defense, 1)
        current_player_hp = player.current_hp
        player.take_damage(damage_to_player)

        print(Fore.RED + f'{enemy.name} hits {player.name} for {current_player_hp - player.current_hp} damage!')
        print(f'{player.name} HP: {player.current_hp}/{player.max_hp}\n')
        time.sleep(delay)

        if not player.is_alive():
            print(Fore.RED + f'{player.name} has fallen...\n')
            return 'defeat'