import random
from ailment.status_ailment import StatusAilment


class FreezeStatusAilment(StatusAilment):
    def whenInflicted(self, pokemon):
        print(pokemon.trainerAndName() + " was frozen solid!")

    def canAttack(self, pokemon):
        if random.random() < 0.2:
            print(pokemon.trainerAndName() + " thawed out!")
            pokemon.ailment = None
            return True
        else:
            print(pokemon.trainerAndName() + " is frozen solid!")
            return False

    def battleMultiplier(self, chance):
        return 1 + 0.5 * chance / 100
