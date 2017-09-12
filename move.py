from effect.effect import Effect
from type import Type
from main.dexLoader import DexLoader

DAMAGE_NONE = "non-damaging"
DAMAGE_PHYSICAL = 'physical'
DAMAGE_SPECIAL = 'special'


class Move(object):
    def __init__(self, dex=None, mid=None):
        if dex is not None:
            self.dex = dex
        else:
            self.dex = DexLoader().movedex
        self.move = self.dex.get(str(mid))

        self.id = self.move.get("id")
        self.name = self.move.get("name")
        self.basePower = self.move.get("power")
        self.type = Type(DexLoader().typedex, self.move.get("type"))
        self.effect = Effect.make(id=self.move.get("effect"), chance=self.move.get("effect_chance"))
        self.accuracy = self.move.get("accuracy") if self.move.get("accuracy") > 0 else 100
        self.priority = self.move.get("priority")
        self.damageClass = self.move.get("damage_class")

    def __str__(self):
        return self.name + "(" + self.type.name + " - " + (
            'X' if self.basePower == 1 else self.basePower) + " power - " + str(self.accuracy) + " accuracy)"

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
        base = self.accuracy / 100
        if self.priority > 0 and lethal:
            base *= 5
        base *= self.effect.battleMultiplier(attacker, defender, damage, lethal)
        return base

    def effectiveness(self, attacker, defender):
        effectiveness = self.type.effectivenessAgainst(defender.types)
        return self.effect.effectiveness(attacker, defender, effectiveness)

    def power(self, attacker=None, defender=None):
        return self.effect.power(base=self.basePower)

    def hits(self):
        return self.effect.hits()

    def criticalRateStage(self):
        return self.effect.criticalRateStage()

    def afterDamage(self, attacker, defender, damage):
        self.effect.afterDamage(attacker, defender, damage)

    def afterMiss(self, attacker, defender):
        self.effect.afterMiss(attacker, defender)


struggle = Move(DexLoader().movedex, 165)

if __name__ == "__main__":
    pass
