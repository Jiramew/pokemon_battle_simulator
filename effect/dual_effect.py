from effect.default_effect import DefaultEffect


class DualEffect(DefaultEffect):
    def __init__(self, id, effects):
        self.id = id
        self.effects = effects

    def effectiveness(self, attacker, defender):
        pass
