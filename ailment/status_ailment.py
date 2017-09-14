class StatusAilment(object):
    def affects(self, pokemon):
        return True

    def whenInflicted(self, pokemon):
        pass

    def whenSwitchedOut(self, pokemon):
        pass

    def canAttack(self, pokemon):
        return True

    def endTurn(self, pokemon):
        pass

    def statMultiplier(self, stat):
        return 1

    def battleMultiplier(self, chance):
        return 1
