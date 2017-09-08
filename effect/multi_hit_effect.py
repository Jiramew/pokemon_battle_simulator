import random
from effect.default_effect import DefaultEffect


class MultiHitEffect(DefaultEffect):
    def __init__(self, id, chance=None):
        super(MultiHitEffect, self).__init__(id, chance)

    def hits(self):
        if self.id == 30:
            return random.sample([2, 2, 3, 3, 4, 5], 1)[0]
        elif self.id in [45, 78]:
            return 2

    def buildMultiplier(self, attacker):
        if self.id == 30:
            return 3.166
        elif self.id in [45, 78]:
            return 2

    def battleMultiplier(self, attacker, defender, damage, lethal):
        if not lethal:
            if self.id == 30:
                return 3.166
            elif self.id in [45, 78]:
                return 2
        else:
            return 1
