class Character:
    def __init__(self,  name: str, max_hp : int, attack : int, defense : int):
        self.name = name
        self._base_max_hp = max_hp
        self._base_attack = attack
        self._base_defense = defense
        self.current_hp = max_hp
        self.status_effects = []

    @property
    def max_hp(self):
        total = self._base_max_hp

        for effect in self.status_effects:
            total = effect.modify_max_hp(value= total)
        return max(1, total)

    @max_hp.setter
    def max_hp(self, value):
        self._base_max_hp = value

    @property
    def attack(self):
        total = self._base_attack

        for effect in self.status_effects:
            total = effect.modify_attack(value= total)
        return max(1, total)

    @attack.setter
    def attack(self, value):
        self._base_attack = value

    @property
    def defense(self):
        total = self._base_defense

        for effect in self.status_effects:
            total = effect.modify_defense(value= total)
        return max(0, total)

    @defense.setter
    def defense(self, value):
        self._base_defense = value

    def take_damage(self, amount : int):
        self.current_hp -= amount
        if self.current_hp < 0:
            self.current_hp = 0

    def add_status_effect(self, effect, log):
        for existing in self.status_effects:
            if existing.name == effect.name:

                if not existing.stackable:
                    existing.duration = max(existing.duration, effect.duration)
                    log.append(f'{self.name}\'s {effect.name} is refreshed!')
                    return
                break

        self.status_effects.append(effect)
        effect.on_apply(target= self, log= log)

    def process_turn_start_effects(self, log):
        for effect in list(self.status_effects):
            effect.on_turn_start(target= self, log= log)

    def process_turn_end_effects(self, log):
        for effect in list(self.status_effects):
            effect.on_turn_end(target= self, log= log)

    def update_status_effects(self, log):
        remaining_effects = []

        for effect in self.status_effects:
            effect.tick()

            if effect.is_expired():
                effect.on_expire(target= self, log= log)
            else:
                remaining_effects.append(effect)
        
        self.status_effects = remaining_effects
    
    def is_alive(self):
        return self.current_hp > 0

    def rescale_current_hp(self, old_max_hp : int):
        new_max_hp = self.max_hp

        if old_max_hp < 1:
            self.current_hp = new_max_hp
            return
    
        ratio = self.current_hp / old_max_hp
        self.current_hp = int(new_max_hp * ratio)

        if self.current_hp > new_max_hp:
            self.current_hp = new_max_hp

    def heal(self, amount: int):
        self.current_hp = min(self.current_hp + amount, self.max_hp)