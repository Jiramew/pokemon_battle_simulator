from ailment.status_ailment import StatusAilment


class BurnStatusAilment(StatusAilment):
    def affects(self, pokemon):
        return "Fire" not in [type.name for type in pokemon.types]

    def whenInflicted(self, pokemon):
        print(pokemon.trainerAndName() + " was burned!")

    def endTurn(self, pokemon):
        damage = round(pokemon.maxHp / 8)
        print("{0} was hurt {1} by its burn!".format(pokemon.name, damage))

    def statMultiplier(self, stat):
        if stat == "attack":
            return 0.5
        else:
            return 1

    def battleMultiplier(self, chance):
        return 1 + 0.5 * chance / 100
