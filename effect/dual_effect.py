from effect.default_effect import DefaultEffect
from functools import reduce


class DualEffect(DefaultEffect):
    def __init__(self, id, chance, effects):
        super(DualEffect, self).__init__(id, chance)
        self.effects = effects

    def power(self, base, attacker=None, defender=None):
        return base

    def effectiveness(self, attacker, defender, effectiveness=None):
        return reduce(lambda x, y: x * y, [effect.effectiveness(attacker, defender) for effect in self.effects])

    def hits(self):
        return max([effect.hits() for effect in self.effects])

    def criticalRateStage(self):
        return max([effect.criticalRateStage() for effect in self.effects])

    def buildMultiplier(self, attacker):
        return reduce(lambda x, y: x * y, [effect.buildMultiple(attacker) for effect in self.effects])

    def battleMultiplier(self, attacker, defender, damage, lethal):
        return reduce(lambda x, y: x * y,
                      [effect.battleMultiplier(attacker, defender, damage, lethal) for effect in self.effects])

    def afterDamage(self, attacker, defender, damage):
        for effect in self.effects:
            effect.afterDamage(attacker, defender, damage)

    def afterMiss(self, attacker, defender):
        for effect in self.effects:
            effect.afterMiss(attacker, defender)
