from ability_templates import ABILITY_TEMPLATES
from status_effect import DamageOverTime, StatModifier

class AbilityResult:
    def __init__(self):
        self.events = []
        self.messages = []

    def add_event(self, event_type : str, **data):
        self.events.append(
            {'type' : event_type, **data}
        )

    def add_damage(self, source, target, amount : int):
        if amount < 1: return

        self.add_event(event_type= 'damage', source= source, target= target, amount= amount)

    def add_healing(self, source, target, amount : int):
        if amount < 1: return

        self.add_event(event_type= 'heal', source= source, target= target, amount= amount)
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
            self._interpret_effect(effect= effect, caster= caster, target= target, result= result)
        return result

    def _has_resources(self, caster):
        for resource, cost in self.resource_cost.items():
            if caster.get_resource(resource_type= resource) < cost:
                return False
        return True

    def _consume_resources(self, caster):
        for resource, cost in self.resource_cost.items():
            caster.spend_resource(resource_type= resource, amount= cost)
    
    def _interpret_effect(self, effect, caster, target, result):

        effect_type = effect['type']

        if effect_type == 'damage':
            stat_value = getattr(caster, effect['stat'])
            damage = int(stat_value * effect.get('multiplier', 1) + effect.get('flat_bonus', 0))

            result.add_damage(source= caster, target= target, amount= damage)

    def _interpret_effect(self, effect, caster, target, result):

        effect_type = effect['type']

        if effect_type == 'damage':
            stat_value = getattr(caster, effect['stat'])
            damage = int(stat_value * effect.get('multiplier', 1) + effect.get('flat_bonus', 0))

            result.add_damage(source= caster, target= target, amount= damage)

        elif effect_type == 'heal':
            stat_value = getattr(caster, effect['stat'])
            amount = int(stat_value * effect.get('multiplier', 1) + effect.get('flat_bonus', 0))

            result.add_healing(source= caster, target= target, amount= amount)

        elif effect_type == 'status_effect':

            effect_class = effect['effect_class']
            duration = effect.get('duration', 1)
            potency = effect.get('potency', 0)
            name = effect.get('name', effect_class)

            if effect_class == 'DamageOverTime':
                status = DamageOverTime(
                    name= name,
                    duration= duration,
                    potency= potency,
                    source= caster
                )

            elif effect_class == 'StatModifier':
                stat = effect['stat']
                amount = effect['amount']

                status = StatModifier(
                    name= name,
                    duration= duration,
                    stat= stat,
                    amount= amount,
                    source= caster
                )

            else:
                return

            result.add_event(event_type= 'status_effect', source= caster, target= target, effect = status)


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