import time
from loot import generate_loot
from colorama import Fore, Style

class BattleResult:
    def __init__(self, result : str, log : list[str], loot= None, is_boss : bool = False):
        self.result = result
        self.log = log
        self.loot = loot
        self.is_boss = is_boss


def mitigate_damage(raw_damage : int, target):
    return max(raw_damage - target.defense, 1)


def apply_ability_result(result, log):
    for event in result.events:

        event_type = event['type']
        source = event['source']
        target = event['target']

        if event_type == 'damage':
            raw = event['amount']
            damage = mitigate_damage(raw_damage= raw, target= target)
            before = target.current_hp
            target.take_damage(amount= damage)

            log.append(Fore.GREEN + f'{target.name} takes {before - target.current_hp} damage!')

        elif event_type == 'heal':
            amount = event['amount']
            before = target.current_hp
            target.current_hp = min(target.current_hp + amount, target.max_hp)

            log.append(Fore.GREEN + f'{target.name} heals {target.current_hp - before} HP!')


menu = {'1' : 'Attack', '2' : 'Ability'}
def player_turn(player, enemy, log):

    while True:
        print('Choose Action')
        for i, v in menu.items():
            print(f'{i}. {v}')
        
        choice = input('> ').strip()

        if not choice.isdigit() or choice not in menu:
            print('Invalid Choice')
            continue

        elif menu[choice] == 'Attack':

            raw = player.attack
            damage = mitigate_damage(raw_damage= raw, target= enemy)
            before = enemy.current_hp
            enemy.take_damage(damage)

            log.append(Fore.GREEN + f'{player.name} strikes {enemy.name} for {before - enemy.current_hp} damage!')

            break
        
        elif menu[choice] == 'Ability':

            while True:
                print('\nAbilities:')

                print('0. Back')

                for i, ability in enumerate(player.abilities, start= 1):
                    cost = ability.resource_cost.get('mana', 0)
                    print(f'{i}. {ability.name} (Mana : {cost}) [You: {player.get_resource(resource_type= "mana")}]')
                
                choice = input('> ').strip()

                if not choice.isdigit():
                    print('Invalid Choice')
                    continue

                if choice == '0':
                    print()
                    break
                
                selection = int(choice) -1

                if selection < 0 or selection >= len(player.abilities):
                    print('Invalid Choice')
                    continue
                
                ability = player.abilities[selection]
                result = ability.use(caster= player, target= enemy)

                for message in result.messages:
                    log.append(message)
                
                apply_ability_result(result= result, log= log)

                return


def battle(player, enemy) -> BattleResult:

    log = []
    name = enemy.name or 'Unknown Creature'

    if enemy.is_boss:
        log.append(Style.BRIGHT + Fore.MAGENTA + f'\nA terrifying presence fills the dungeon...')
        log.append(Style.BRIGHT + Fore.MAGENTA + f'{name} emerges from the shadows!\n')
        log.append(Style.BRIGHT + Fore.MAGENTA + f'{name} HP: {enemy.current_hp}/{enemy.max_hp}\n')
    else:
        article = 'an' if name[0].lower() in 'aeiou' else 'a'
        log.append(f'\n{player.name} encounters {article} {name}!')
        log.append(f'{name} HP: {enemy.current_hp}/{enemy.max_hp}\n')

    flush_log(log= log, delay= 1)

    while player.is_alive() and enemy.is_alive():

        player_turn(player= player, enemy= enemy, log= log)

        log.append(f'{name} HP: {enemy.current_hp}/{enemy.max_hp}\n')

        flush_log(log= log)

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


        raw = enemy.attack
        damage_to_player = mitigate_damage(raw_damage= raw, target= player)
        current_player_hp = player.current_hp
        player.take_damage(damage_to_player)

        log.append(Fore.RED + f'{enemy.name} hits {player.name} for {current_player_hp - player.current_hp} damage!')
        log.append(f'{player.name} HP: {player.current_hp}/{player.max_hp}\n')

        flush_log(log= log)

        if not player.is_alive():
            log.append(Fore.RED + f'{player.name} has fallen...\n')
            return BattleResult(
                result= 'defeat',
                log= log,
                loot= None,
                is_boss= enemy.is_boss
            )


def flush_log(log, delay= 0.5):
    for line in log:
        print(line)
        time.sleep(delay)
    log.clear()