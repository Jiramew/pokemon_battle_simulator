from effect.default_effect import DefaultEffect


class WeightDependentEffect(DefaultEffect):
    def __init__(self, id, chance=None):
        super(WeightDependentEffect, self).__init__(id, chance)

    def power(self, base, attacker=None, defender=None):
        if defender is None:
            return 60
        else:
            if defender.weight < 10:
                return 20
            elif defender.weight < 25:
                return 40
            elif defender.weight < 50:
                return 60
            elif defender.weight < 100:
                return 80
            elif defender.weight < 200:
                return 100
            else:
                return 200
