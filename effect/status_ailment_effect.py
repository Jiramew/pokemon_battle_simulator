import random
from effect.default_effect import DefaultEffect
from ailment.poison_status_ailment import PoisonStatusAilment
from ailment.bad_poison_status_ailment import BadPoisonStatusAilment
from ailment.burn_status_ailment import BurnStatusAilment
from ailment.freeze_status_ailment import FreezeStatusAilment
from ailment.paralysis_status_ailment import ParalysisStatusAilment


class StatusAilmentEffect(DefaultEffect):
    def ailment(self):
        if self.id in [3, 78, 210]:
            return PoisonStatusAilment()
        if self.id in [5, 201, 254, 274]:
            return BurnStatusAilment()
        if self.id in [6, 261, 275]:
            return FreezeStatusAilment()
        if self.id in [7, 153, 263, 276]:
            return ParalysisStatusAilment()
        if self.id == 203:
            return BadPoisonStatusAilment()

    def buildMultiplier(self, attacker):
        ailment = self.ailment()
        return ailment.battleMultiplier(self.chance)

    def battleMultiplier(self, attacker, defender, damage, lethal):
        ailment = self.ailment()
        if not defender.ailment and ailment.affects(defender):
            return ailment.battleMultiplier(self.chance)
        else:
            return 1

    def afterDamage(self, attacker, defender, damage):
        if defender.ailment or (not defender.isAlive()):
            pass
        ailment = self.ailment()
        if ailment.affects(defender) and random.random() * 100 < self.chance:
            defender.ailment = ailment
            ailment.whenInflicted(defender)
