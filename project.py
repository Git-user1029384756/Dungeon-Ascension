import random, os
from enemy import Enemy
from player import Player
from combat import battle
from colorama import init, Fore, Style
from art import intro_banner_art, death_art, boss_art
from save_load import load_characters, save_characters
from config import CLASS_STATS, ENEMY_STATS, FLOOR_ENEMIES, VICTORIES_REQUIRED, MAX_FLOOR

init(autoreset=True)

def main():
    character_data = load_characters()

    print(Fore.GREEN + intro_banner_art())

    if character_data:
        print('Existing Characters - Input their exact name to select\n')
        for num, char in enumerate(character_data, start= 1):
            print(f'{num}- {Style.BRIGHT + char}')
        print()

    player_name = input('Select a Character or create a new one : ')

    if player_name in character_data:
        player = Player.from_dict(name= player_name, data= character_data[player_name])

    else:
        classes = {num : clas for num, clas in enumerate(CLASS_STATS, start= 1)}
        for i, v in classes.items():
            print(f'{i} - {v.title()}')

        while True:
            choice = input('Choose Class : ').strip().lower()
            player_class = None

            if choice.isdigit():
                if 0 < int(choice) <= len(classes):
                    player_class = int(choice)
                    player = Player(
                        name= player_name,
                        class_type= classes[player_class],
                        max_hp= CLASS_STATS[classes[player_class]]['max_hp'],
                        attack= CLASS_STATS[classes[player_class]]['attack'],
                        defense= CLASS_STATS[classes[player_class]]['defense']
                        )

            elif choice in CLASS_STATS:
                player_class = choice
                player = Player(
                    name= player_name,
                    class_type= player_class,
                    max_hp= CLASS_STATS[player_class]['max_hp'],
                    attack= CLASS_STATS[player_class]['attack'],
                    defense= CLASS_STATS[player_class]['defense']
                    )

            if player_class:
                break
            else:
                print('Invalid class. Select from the classes given.')

    clear_terminal()


    menu = {'1' :'Explore Floor', '2' : 'Use Potion', '3' : 'View Stats', '4' : 'Exit'}

    while True:
        for i, v in menu.items():
            print(f'{i}. {v}')

        while True:
            option = input('Choose an option : ').strip()
            if option in menu:
                break
            print('Invalid Option, select a number.')

        if menu[option] == 'Exit':
            clear_terminal()
            break

        elif menu[option] == 'Use Potion':
            player.use_potion()

        elif menu[option] == 'View Stats':
            clear_terminal()
            player.display_stats()
            input('\nPress Enter to continue...')
            clear_terminal()

        elif menu[option] == 'Explore Floor':
            roll = random.random()

            if roll < .65:
                enemy = create_enemy_for_floor(player.current_floor)
                battle_result = battle(player= player, enemy= enemy)

                if battle_result == 'defeat':
                    player.current_hp = player.max_hp
                    player.victories_on_floor = 0
                    clear_terminal()
                    print(Fore.RED + death_art())
                    print(Style.BRIGHT + Fore.RED + '\nYour vision fades…\nYour soul escapes the dungeon…\nYou awaken once more…')

                    lower_floor = calculate_new_floor_on_defeat(player.current_floor)

                    if player.current_floor > lower_floor:
                        player.current_floor = lower_floor
                        print(f'\n{player.name} will be revived in the previous Floor.')
                    break

                else:
                    print(f'Earned {enemy.xp_reward} xp')
                    player.add_xp(amount= enemy.xp_reward)
                    player.victories_on_floor += 1
                    print(f'Victory, current level is {player.level} and current xp is {player.xp}\n')

                    if should_descend_floor(player.victories_on_floor, player.current_floor):
                        player.victories_on_floor = 0
                        clear_terminal()
                        print(Fore.CYAN + f'The air grows heavier…\nYou descend deeper into the dungeon…\n')
                        player.current_floor += 1
                    elif player.current_floor == MAX_FLOOR:
                        print(Style.BRIGHT + Fore.MAGENTA + 'Max Floor reached.\nResetting back to Floor 1\n')
                        player.current_floor = 1
                        player.victories_on_floor = 0

            elif roll < .9:
                player.inventory['Potion'] += 1
                print(f'\nYou find a potion while exploring the dungeon.\nYou now have {player.inventory["Potion"]} potion(s)\n')

            else:
                print('\nYou come across an empty room. Nothing interesting happens.\n')


    character_data[player_name] = player.to_dict()

    save_characters(character_data)


def create_enemy_for_floor(floor : int):
    enemy_name = random.choice(FLOOR_ENEMIES[floor])
    enemy_data = ENEMY_STATS[enemy_name]
    display_name = enemy_data.get('display_name', enemy_name.title())

    enemy = Enemy(
        name= display_name,
        max_hp= enemy_data['max_hp'],
        attack= enemy_data['attack'],
        defense= enemy_data['defense'],
        xp_reward= enemy_data['xp_reward'],
        is_boss= enemy_data.get('is_boss', False)
        )

    if enemy.is_boss:
        if enemy.name.lower() in boss_art:
            clear_terminal()
            print(Fore.BLUE + boss_art[enemy.name.lower()]())

    return enemy


def should_descend_floor(victories_on_floor : int, current_floor : int):
    if current_floor < MAX_FLOOR and victories_on_floor == VICTORIES_REQUIRED:
        return True
    return False


def calculate_new_floor_on_defeat(current_floor : int):
    if current_floor > 1:
        return current_floor - 1
    return current_floor


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main()
