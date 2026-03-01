import random, os
from enemy import Enemy
from combat import battle
from player import Player
from colorama import Fore, Style, init
from art import intro_banner_art, death_art, boss_art
from save_load import load_characters, save_characters
from config import CLASS_STATS, ENEMY_STATS, FLOOR_ENEMIES, VICTORIES_REQUIRED, MAX_FLOOR

init(autoreset=True)


class GameEngine:
    def __init__(self):
        self.player = None
        self.character_data = {}
        self.running = True


    def start(self):
        self.running = True
        self.character_data = load_characters()
        print(Fore.GREEN + intro_banner_art())
        self.select_or_create_player()
        clear_terminal()
        self.game_loop()
        self.save_game()
    

    def select_or_create_player(self):
        if self.character_data:
            print('Existing Characters - Input their exact name to select\n')
            for num, char in enumerate(self.character_data, start= 1):
                print(f'{num}- {Style.BRIGHT + char}')
            
        print()
        player_name = input('Select a Character or create a new one : ')

        if player_name in self.character_data:
            self.player = Player.from_dict(name= player_name, data= self.character_data[player_name])
        else:
            classes = {num : clas for num, clas in enumerate(CLASS_STATS, start= 1)}
            for num, name in classes.items():
                print(f'{num} - { Style.BRIGHT + name.title()}')

            while True:
                choice = input('Choose Class : ').strip().lower()
                player_class = None

                if choice.isdigit():
                    if 0 < int(choice) <= len(classes):
                        player_class = int(choice)
                        self.player = Player(
                            name= player_name,
                            class_type= classes[player_class],
                            max_hp= CLASS_STATS[classes[player_class]]['max_hp'],
                            attack= CLASS_STATS[classes[player_class]]['attack'],
                            defense= CLASS_STATS[classes[player_class]]['defense']
                            )

                elif choice in CLASS_STATS:
                    player_class = choice
                    self.player = Player(
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


    def game_loop(self):
        menu = {'1' :'Explore Floor', '2' : 'Use Potion', '3' : 'View Stats', '4' : 'Exit'}

        while self.running:
            for num, value in menu.items():
                print(f'{num}. {value}')
            
            while True:
                option = input('Choose an option : ').strip()
                if option in menu:
                    break
                print('Invalid Option, select a number.')
            
            if menu[option] == 'Exit':
                clear_terminal()
                self.running = False

            elif menu[option] == 'Use Potion':
                self.player.use_potion()
            
            elif menu[option] == 'View Stats':
                clear_terminal()
                self.player.display_stats()
                input('\nPress Enter to continue...\n')

            elif menu[option] == 'Explore Floor':
                self.explore()


    def explore(self):
        encounter = self.roll_encounter_type()

        if encounter == 'combat':
            enemy = self.create_enemy_for_floor(floor= self.player.current_floor)
            battle_result = battle(player= self.player, enemy= enemy)

            if battle_result == 'defeat':
                self.player.current_hp = self.player.max_hp
                self.player.victories_on_floor = 0
                clear_terminal()
                print(Fore.RED + death_art())
                print(Style.BRIGHT + Fore.RED + '\nYour vision fades…\nYour soul escapes the dungeon…\nYou awaken once more…')

                lower_floor = self.calculate_new_floor_on_defeat(current_floor= self.player.current_floor)

                if self.player.current_floor > lower_floor:
                    self.player.current_floor = lower_floor
                    print(f'\n{self.player.name} will be revived in the previous Floor.')
                self.running = False

            else:
                print(f'Earned {enemy.xp_reward} xp')
                self.player.add_xp(amount= enemy.xp_reward)
                self.player.victories_on_floor += 1
                print(f'Victory, current level is {self.player.level} and current xp is {self.player.xp}\n')

                if self.should_descend_floor(victories_on_floor= self.player.victories_on_floor, current_floor= self.player.current_floor):
                    self.player.victories_on_floor = 0
                    clear_terminal()
                    print(Fore.CYAN + f'The air grows heavier…\nYou descend deeper into the dungeon…\n')
                    self.player.current_floor += 1

                elif self.player.current_floor == MAX_FLOOR:
                    print(Style.BRIGHT + Fore.MAGENTA + 'Max Floor reached.\nResetting back to Floor 1\n')
                    self.player.current_floor = 1
                    self.player.victories_on_floor = 0

        elif encounter == 'potion':
            self.player.inventory['Potion'] += 1
            print(f'\nYou find a potion while exploring the dungeon.\nYou now have {self.player.inventory["Potion"]} potion(s)\n')            

        else:
            print('\nYou come across an empty room. Nothing interesting happens.\n')
    

    def roll_encounter_type(self):
        roll = random.random()
        if roll < .65:
            return 'combat'
        elif roll < .9:
            return 'potion'
        else:
            return 'empty'


    def create_enemy_for_floor(self, floor : int):
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


    def should_descend_floor(self, victories_on_floor : int, current_floor : int):
        if current_floor < MAX_FLOOR and victories_on_floor == VICTORIES_REQUIRED:
            return True
        return False


    def calculate_new_floor_on_defeat(self, current_floor : int):
        if current_floor > 1:
            return current_floor - 1
        return current_floor
    

    def save_game(self):
        self.character_data[self.player.name] = self.player.to_dict()         
        save_characters(self.character_data)


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    engine = GameEngine()
    engine.start()