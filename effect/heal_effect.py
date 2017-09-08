from effect.default_effect import DefaultEffect


class HealEffect(DefaultEffect):
    def __init__(self, id, chance=None):
        super(HealEffect, self).__init__(id, chance)

    def heal(self, damage):
        if self.id in [4, 348]:
            return round(damage * 0.5)
        elif self.id == 353:
            return round(damage * 0.75)

    def buildMultiplier(self, attacker):
        if self.id in [4, 348]:
            return 1.25
        elif self.id == 353:
            return 1.5

    def battleMultiplier(self, attacker, defender, damage, lethal):
        if attacker.hp < attacker.maxHp:
            return 1 + self.heal(damage) / (attacker.maxHp - attacker.hp) / 1.5
        else:
            return 1

    def afterDamage(self, attacker, defender, damage):
        heal = min([self.heal(damage), attacker.maxHp - attacker.hp])

        if heal != 0:
            attacker.hp += heal
        else:
            return
