from ailment.poison_status_ailment import PoisonStatusAilment


class BadPoisonStatusAilment(PoisonStatusAilment):
    def __init__(self):
        self.multiplier = 1 / 16

    def whenSwitchedOut(self, pokemon):
        self.multiplier = 1 / 16

    def whenInflicted(self, pokemon):
        print(pokemon.trainerAndName() + " was badly poisoned!")

    def endTurn(self, pokemon):
        super().endTurn(pokemon)
        self.multiplier += 1 / 16

    def battleMultiplier(self, chance):
        return 1 + 0.66 * chance / 100
