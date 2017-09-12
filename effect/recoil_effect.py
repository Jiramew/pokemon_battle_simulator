from effect.default_effect import DefaultEffect


class RecoilEffect(DefaultEffect):
    def __init__(self, id, chance=None):
        super(RecoilEffect, self).__init__(id, chance)

    def recoil(self, damage, pokemon=None):
        if self.id == 49:
            return round(damage / 4)
        elif self.id in [199, 254, 263]:
            return round(damage / 3)
        elif self.id == 270:
            return round(damage / 2)
        else:
            return 0

    def buildMultiplier(self, attacker):
        if self.id in [49, 199, 254, 263]:
            return 0.85
        elif self.id == 270:
            return 0.5

    def battleMultiplier(self, attacker, defender, damage, lethal):
        return 1 - self.recoil(damage, attacker) / attacker.hp / 1.5

    def afterDamage(self, attacker, defender, damage):
        attacker.takeDamage(self.recoil(damage), attacker)
