from effect.default_effect import DefaultEffect


class StruggleEffect(DefaultEffect):
    def __init__(self, id, chance=None):
        super(StruggleEffect, self).__init__(id, chance)

    def recoil(self, damage, pokemon):
        return round(pokemon.maxHp / 4)

    def effectiveness(self, attacker, defender, effectiveness):
        return 1
