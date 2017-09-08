from effect.default_effect import DefaultEffect


class CritRateEffect(DefaultEffect):
    def __init__(self, id, chance=None):
        super(CritRateEffect, self).__init__(id, chance)

    def criticalRateStage(self):
        if self.id in [44, 201, 210]:
            return 1
        elif self.id == 289:
            return 50

    def buildMultiplier(self, attacker):
        if self.id in [44, 201, 210]:
            return 1.03
        elif self.id == 289:
            return 1.5

    def battleMultiplier(self, attacker, defender, damage, lethal):
        if self.id in [44, 201, 210]:
            return 1.03
        elif self.id == 289:
            return 1.5
