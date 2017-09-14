import random
from ailment.status_ailment import StatusAilment


class ParalysisStatusAilment(StatusAilment):
    def affects(self, pokemon):
        return 'Electric' not in [type.name for type in pokemon.types]

    def whenInflicted(self, pokemon):
        print(pokemon.trainerAndName() + " was paralyzed! It may be unable to move!")

    def canAttack(self, pokemon):
        if random.random() < 0.25:
            print(pokemon.trainerAndName() + " is paralyzed! It can't move!")
            return False

    def statMultiplier(self, stat):
        if stat == "speed":
            return 0.25
        else:
            return 1

    def battleMultiplier(self, chance):
        return 1 + 0.5 * chance / 100
