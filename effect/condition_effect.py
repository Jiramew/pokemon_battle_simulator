import random
from effect.default_effect import DefaultEffect
from condition.flinch_condition import FlinchCondition
from condition.confusion_condition import ConfusionCondition


class ConditionEffect(DefaultEffect):
    def condition(self):
        if self.id in [32, 147, 151, 274, 275, 276]:
            return FlinchCondition()
        elif self.id in [77, 268, 338]:
            return ConfusionCondition()

    def buildMultiplier(self, attacker):
        condition = self.condition()
        return condition.buildMultiplier(attacker, self.chance)

    def battleMultiplier(self, attacker, defender, damage, lethal):
        condition = self.condition()
        if not condition.isInflicted(defender):
            return condition.battleMultiplier(attacker, defender, self.chance)
        else:
            return 1

    def afterDamage(self, attacker, defender, damage):
        if not defender.isAlive():
            pass
        condition = self.condition()
        if not condition.isInflicted(defender) and random.random() * 100 < self.chance:
            condition.inflict(defender)
