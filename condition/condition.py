class Condition(object):
    def __init__(self):
        self.name = self.__class__.__name__

    def inflict(self, pokemon):
        key = self.name
        pokemon.conditions[key] = self
        self.whenInflicted(pokemon)

    def isInflicted(self, pokemon):
        key = self.name
        if key in pokemon.conditions:
            return pokemon.conditions[key]
        else:
            return False

    def heal(self, pokemon):
        key = self.name
        del pokemon.conditions[key]

    def whenInflicted(self, pokemon):
        pass

    def canAttack(self, pokemon):
        return True

    def endTurn(self, pokemon):
        pass

    def buildMultiplier(self, attacker, chance):
        return 1

    def battleMultiplier(self, attacker, defender, chance):
        return 1
