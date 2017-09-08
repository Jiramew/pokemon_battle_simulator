from effect.default_effect import DefaultEffect


class NoEffect(DefaultEffect):
    def __init__(self, id, chance=None):
        super(NoEffect, self).__init__(id, chance)


if __name__ == "__main__":
    ne = NoEffect(1)
