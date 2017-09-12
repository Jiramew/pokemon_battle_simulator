from effect.default_effect import DefaultEffect
from functools import reduce
import random


class StatStageEffect(DefaultEffect):
    def __init__(self, id, chance=None):
        super(StatStageEffect, self).__init__(id, chance)

    def target(self, attacker, defender):
        if self.id in [139, 140, 141, 205, 219, 230, 277, 296, 335]:
            return attacker
        elif self.id in [21, 69, 70, 71, 72, 73, 272, 297, 331]:
            return defender

    def stats(self):
        if self.id == 69:
            return {"attack": -1}
        if self.id == 70:
            return {"defense": -1}
        if self.id == 72:
            return {"spattack": -1}
        if self.id == 73:
            return {"spdefense": -1}
        if self.id in [21, 71, 331]:
            return {"speed": -1}
        if self.id == 140:
            return {"attack": 1}
        if self.id == 139:
            return {"defense": 1}
        if self.id == 277:
            return {"spattack": 1}
        if self.id in [219, 296]:
            return {"speed": 1}
        if self.id == 205:
            return {"spattack": -2}
        if self.id in [272, 297]:
            return {"spdefense": -2}
        if self.id == 230:
            return {"defense": -1, "spdefense": -1}
        if self.id == 335:
            return {"defense": -1, "spdefense": -1, "speed": -1}
        if self.id == 141:
            return {"attack": 1, "spattack": 1, "defense": 1, "spdefense": 1, "speed": 1}

    def buildMultiplier(self, attacker):
        totalchanges = reduce(lambda x, y: x + y, [v for (k, v) in self.stats().items()])
        if self.target(True, False):
            return 1 + 0.25 * totalchanges * self.chance / 100
        else:
            return 1 - 0.25 * totalchanges * self.chance / 100

    def battleMultiplier(self, attacker, defender, damage, lethal):
        return self.buildMultiplier(attacker)

    def afterDamage(self, attacker, defender, damage):
        target = self.target(attacker, defender)
        if random.random() * 100 < self.chance and target.isAlive():
            for stat, change in self.stats().items():
                target.modifyStatStage(stat, change)
