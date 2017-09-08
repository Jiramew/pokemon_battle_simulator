from effect.default_effect import DefaultEffect


class DoublePowerEffect(DefaultEffect):
    def __init__(self, id, chance=None):
        super(DoublePowerEffect, self).__init__(id, chance)

    def power(self, base):
        return base * 2
