from effect.effect import Effect
from type import Type
from main.dexLoader import DexLoader

DAMAGE_NONE = "non-damaging"
DAMAGE_PHYSICAL = 'physical'
DAMAGE_SPECIAL = 'special'


class Move(object):
    def __init__(self, dex, mid):
        self.dex = dex
        self.struggle = Move(dex, 165)
        self.move = self.dex.get(str(mid))

        self.id = self.move.id
        self.name = self.move.name
        self.type = Type(self.dex, self.move.type)
        self.basePower = self.power()
        self.accurary = self.move.accurary if self.move.accurary > 0 else 100
        self.priority = self.move.priority
        self.effect = Effect.make(id=self.move.effect, chance=self.move.effect_chance)
        self.damageClass = self.move.damage_class

    def __str__(self):
        return self.name + "(" + self.type.name + " - " + (
            'X' if self.basePower == 1 else self.basePower) + " power - " + str(self.accurary) + " accuracy)"

    def banned(self):
        return (self.damageClass == DAMAGE_NONE) or (self.effect.banned()) or (self.power() < 2)

    def attackStat(self):
        return "attack" if self.damageClass == DAMAGE_PHYSICAL else "spattack"

    def defenseStat(self):
        return "defense" if self.damageClass == DAMAGE_PHYSICAL else "spdefense"

    def buildMultiplier(self, attacker):
        base = self.effect.buildMultiplier(attacker)

        return base * 1.33 if self.priority > 0 else base * 0.9

    def battleMultiplier(self, attacker, defender, damage):
        lethal = damage >= defender.hp
        base = self.accurary / 100
        if self.priority > 0 and lethal:
            base *= 5
        base *= self.effect.battleMultiplier(attacker, defender, damage, lethal)

    def effectiveness(self, attacker, defender):
        effectiveness = self.type.effectivenessAgainst(defender.types)
        return self.effect.effectiveness(attacker, defender, effectiveness)

    def power(self, attacker=None, defender=None):
        return self.effect.power(self.basePower, attacker, defender)

    def hits(self):
        return self.effect.hits()

    def criticalRateStage(self):
        return self.effect.criticalRateStage()

    def afterDamage(self, attacker, defender, damage):
        self.effect.afterDamage(attacker, defender, damage)

    def afterMiss(self, attacker, defender):
        self.effect.afterMiss(attacker, defender)


if __name__ == "__main__":
    pass
