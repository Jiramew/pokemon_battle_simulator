from condition.condition import Condition


class FlinchCondition(Condition):
    def endTurn(self, pokemon):
        self.heal(pokemon)

    def canAttack(self, pokemon):
        print(pokemon.trainerAndName() + " flinched and couldn't move!")
        return False

    def buildMultiplier(self, attacker, chance):
        if attacker.stats.get("base").get("speed") >= 80:
            return 1 + 0.2 * chance / 30
        else:
            return 1

    def battleMultiplier(self, attacker, defender, chance):
        if attacker.speed() > defender.speed():
            return 1 + 0.2 * chance / 30
        else:
            return 1
