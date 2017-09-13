import random


class DamageCalculator(object):
    def __init__(self):
        pass

    def calculate(self, move, attacker, defender, critical=False, rand=0.9):
        attack = attacker.stat(move.attackStat(), {"ignoreNegative": critical})
        defense = defender.stat(move.defenseStat(), {"ignorePositive": critical})

        stab = 1.5 if move.type.id in [type.id for type in attacker.types] else 1
        type = move.effectiveness(attacker, defender)
        crit = 1.5 if critical else 1

        return self.formula(move.power(attacker, defender), attack, defense, stab * type * crit * rand)

    def confusionDamage(self, pokemon):
        attack = pokemon.stat("attack")
        defense = pokemon.stat("defense")
        rand = random.random() * (1 - 0.85) + 0.85

        return self.formula(40, attack, defense, rand)

    def formula(self, power, attack, defense, multiplier):
        return round((0.88 * (attack / defense) * power + 2) * multiplier)
