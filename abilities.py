from ability_templates import ABILITY_TEMPLATES

class AbilityResult:
    def __init__(self):
        self.damage_events = []
        self.healing_events = []
        self.messages = []

    def add_damage(self, amount : int):
        if amount < 1: return
        
        self.damage_events.append(
            {'amount' : amount}
        )

    def add_healing(self, amount : int):
        if amount < 1: return

        self.healing_events.append(
            {'amount' : amount}
        )

    def add_message(self, text : str):
        self.messages.append(text)


class Ability:
    def __init__(self, template_id : str, name : str, target_type : str, effects : list, resource_cost : dict | None = None):
        self.template_id = template_id
        self.name = name
        self.effects = effects
        self.resource_cost = resource_cost if resource_cost is not None else {}
        self.target_type = target_type
    
    def use(self, caster, target):
        result = AbilityResult()

        if not self._has_resources(caster= caster):
            result.add_message(f'You fail to gather the necessary power.')
            return result
        
        self._consume_resources(caster= caster)
        
        result.add_message(text= f'{caster.name} uses {self.name}!')

        for effect in self.effects:
            if effect['type'] == 'damage':
                stat_value = getattr(caster, effect['stat'])
                damage = int(stat_value * effect.get('multiplier', 1) + effect.get('flat_bonus', 0))

                result.add_damage(amount= damage)

        return result
    
    def _has_resources(self, caster):
        for resource, cost in self.resource_cost.items():
            if caster.get_resource(resource_type= resource) < cost:
                return False
        return True
    
    def _consume_resources(self, caster):
        for resource, cost in self.resource_cost.items():
            caster.spend_resource(resource_type= resource, amount= cost)


def ability_from_template(template_id : str):
    template = ABILITY_TEMPLATES.get(template_id)

    if template is None: return

    return Ability(
        template_id= template['template_id'],
        name= template['name'],
        target_type= template['target_type'],
        effects= template['effects'],
        resource_cost= template.get('resource_cost')
    )