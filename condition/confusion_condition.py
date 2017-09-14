import random
from condition.condition import Condition
from mechanism.damage_calculator import DamageCalculator


class ConfusionCondition(Condition):
    def whenInflicted(self, pokemon):
        self.turnsLeft = random.randint(0, 3)

    def canAttack(self, pokemon):
        if self.turnsLeft == 0:
            print(pokemon.trainerAndName() + " snapped out its confusion!")
            self.heal(pokemon)
        else:
            print(pokemon.trainerAndName() + " is confused!")
            self.turnsLeft -= 1
            if random.random() < 0.5:
                damageCalculator = DamageCalculator()
                damage = damageCalculator.confusionDamage(pokemon)
                pokemon.takeDamage(damage, "It hurt itself {0} in its confusion!".format(damage))
                return False

            return True

    def buildMultiplier(self, attacker, chance):
        return 1 + 0.4 * chance / 100

    def battleMultiplier(self, attacker, defender, chance):
        return self.buildMultiplier(attacker, chance)
