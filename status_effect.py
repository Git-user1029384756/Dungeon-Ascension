class StatusEffect:
    def __init__(self, name : str, duration : int, potency : int = 0, source= None):
        self.name = name
        self.duration = duration
        self.potency = potency
        self.source = source
        self.stackable = True
    
    def on_apply(self, target, log):
        pass

    def on_turn_start(self, target, log):
        pass

    def on_turn_end(self, target, log):
        pass

    def on_expire(self, target, log):
        log.append(f'{self.name} on {target.name} has worn off!')

    def tick(self):
        if self.duration > 0:
            self.duration -= 1

    def is_expired(self):
        return self.duration <= 0
    
    def modify_attack(self, value):
        return value
    
    def modify_defense(self, value):
        return value
    
    def modify_max_hp(self, value):
        return value

    def get_turn_text(self, turns):
        return 'turn' if turns == 1 else 'turns'



class DamageOverTime(StatusEffect):
    def __init__(self, name, duration, potency = 0, source=None):
        super().__init__(name, duration, potency, source)

        self.stackable = False

    def on_apply(self, target, log):
        log.append(f'{target.name} is {self.name} ({self.duration} turns)!')

    def on_turn_start(self, target, log):
        if not target.is_alive():
            return
        
        before = target.current_hp
        target.take_damage(self.potency)
        damage = before - target.current_hp

        remaining = self.duration - 1

        if remaining > 0:
            turn_text = self.get_turn_text(turns= remaining)
            log.append(f'{target.name} suffers {damage} damage from {self.name}! ({remaining} {turn_text} left)')
        else:
            log.append(f'{target.name} suffers {damage} damage from {self.name}!')



class StatModifier(StatusEffect):
    def __init__(self, name, duration, stat, amount, source=None):
        super().__init__(name= name, duration= duration, potency= 0, source= source)

        self.stat = stat
        self.amount = amount

    def modify_attack(self, value):
        if self.stat == 'attack':
            return value + self.amount
        return value

    def modify_defense(self, value):
        if self.stat == 'defense':
            return value + self.amount
        return value

    def modify_max_hp(self, value):
        if self.stat == 'max_hp':
            return value + self.amount
        return value

    def on_apply(self, target, log):
        log.append(f'{target.name}\'s {self.stat} is modified by {self.amount}! ({self.duration} turns)!')

    def on_turn_start(self, target, log):
        remaining = self.duration - 1

        if remaining > 0:
            turn_text = self.get_turn_text(turns= remaining)
            log.append(f'{target.name}\'s {self.stat} is still modified by {self.amount}! ({remaining} {turn_text} left)')
        else:
            log.append(f'{target.name}\'s {self.stat} is still modified by {self.amount}!')