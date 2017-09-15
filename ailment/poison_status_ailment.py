from ailment.status_ailment import StatusAilment


class PoisonStatusAilment(StatusAilment):
    def __init__(self):
        self.multiplier = 1 / 8

    def affects(self, pokemon):
        types = [type.name for type in pokemon.types]
        return ("Poison" not in types) and ("Steel" not in types)

    def whenInflicted(self, pokemon):
        print(pokemon.trainerAndName() + " was poisoned!")

    def endTurn(self, pokemon):
        damage = round(pokemon.maxHp * self.multiplier)
        pokemon.takeDamage(damage, "{0} was hurt {1} by poison!".format(str(pokemon), damage))

    def battleMultiplier(self, chance):
        return 1 + 0.4 * chance / 100
