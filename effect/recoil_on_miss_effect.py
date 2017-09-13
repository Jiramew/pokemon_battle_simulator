from effect.default_effect import DefaultEffect


class RecoilOnMissEffect(DefaultEffect):
    def __init__(self, id, chance=None):
        super(RecoilOnMissEffect, self).__init__(id, chance)

    def buildMultiplier(self, attacker):
        return 0.9

    def battleMultiplier(self, attacker, defender, damage, lethal):
        return 0.9

    def afterMiss(self, attacker, defender):
        recoil = min(int(attacker.maxHp / 2), attacker.hp)
        attacker.hp -= recoil

        print(attacker.trainerAndName() + " kept going and crashed for " + str(recoil) + " HP (" + str(
            round(recoil / attacker.maxHp * 100)) + "%)!")
