class DefaultEffect(object):
    def __init__(self, id, chance=None):
        self.id = id
        self.chance = chance

    def power(self, base, attacker=None, defender=None):
        return base

    def effectiveness(self, attacker, defender, effectiveness):
        return effectiveness

    def hits(self):
        return 1

    def criticalRateStage(self):
        return 1

    def buildMultiplier(self, attacker):
        return 1

    def battleMultiplier(self, attacker, defender, damage, lethal):
        return 1

    def afterDamage(self, attacker, defender, damage):
        pass

    def afterMiss(self, attacker, defender):
        pass

    def banned(self):
        return False

    def fullSupport(self):
        return self.__class__.__name__ != "DefaultEffect"


if __name__ == "__main__":
    de = DefaultEffect(1, 2)
