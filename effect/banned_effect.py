from effect.default_effect import DefaultEffect


class BannedEffect(DefaultEffect):
    def __init__(self, id, chance=None):
        super(BannedEffect, self).__init__(id, chance)

    def banned(self):
        return True
