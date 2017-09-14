from effect.banned_effect import BannedEffect
from effect.crit_rate_effect import CritRateEffect
from effect.condition_effect import ConditionEffect
from effect.double_power_effect import DoublePowerEffect
from effect.dual_effect import DualEffect
from effect.default_effect import DefaultEffect
from effect.heal_effect import HealEffect
from effect.multi_hit_effect import MultiHitEffect
from effect.no_effect import NoEffect
from effect.recoil_effect import RecoilEffect
from effect.recoil_on_miss_effect import RecoilOnMissEffect
from effect.stat_stage_effect import StatStageEffect
from effect.struggle_effect import StruggleEffect
from effect.switch_out_effect import SwitchOutEffect
from effect.status_ailment_effect import StatusAilmentEffect
from effect.weight_dependent_effect import WeightDependentEffect


class Effect(object):
    def __init__(self):
        pass

    @staticmethod
    def make(id, chance):
        if id in [1, 35, 104]:
            return NoEffect(id)
        if id in [254, 263]:
            return DualEffect(id, [RecoilEffect(id), StatusAilmentEffect(id, chance)])
        if id == 78:
            return DualEffect(id, [MultiHitEffect(id), StatusAilmentEffect(id, chance)])
        if id in [274, 275, 276]:
            return DualEffect(id, [ConditionEffect(id, chance), StatusAilmentEffect(id, chance)])
        if id in [201, 210]:
            return DualEffect(id, [CritRateEffect(id), StatusAilmentEffect(id, chance)])

        # Status Ailments - Also 126
        if id in [3, 5, 6, 7, 153, 203, 261]:
            return StatusAilmentEffect(id, chance)

        if id in [37, 126, 153, 170, 172, 198, 284, 330]:
            return DefaultEffect(id)

        # Stat Levels
        if id in [74, 304, 305, 306, 344]:
            return DefaultEffect(id)

        if id in [18, 79]:
            return DefaultEffect(id)

        if id in [106, 189, 225, 315]:
            return DefaultEffect(id)

        if id == 229:
            return SwitchOutEffect(id)

        # Misc
        if id in [130, 148, 150, 186, 187, 208, 222, 224, 231, 232, 258, 269, 288, 290, 302, 303, 311, 314, 320, 350]:
            return DefaultEffect(id)

        if id in [32, 147, 151]:
            return ConditionEffect(id, chance)

        if id in [77, 268, 338]:
            return ConditionEffect(id, chance)

        # Fully Implemented
        if id in [4, 348, 353]:
            return HealEffect(id)

        if id in [49, 199, 270]:
            return RecoilEffect(id)

        if id == 46:
            return RecoilOnMissEffect(id)

        if id == 255:
            return StruggleEffect(id)
        if id in [30, 45]:
            return MultiHitEffect(id)
        if id == 318:
            return DoublePowerEffect(id)
        if id == 197:
            return WeightDependentEffect(id)
        if id in [44, 289]:
            return CritRateEffect(id)
        if id in [21, 69, 70, 71, 72, 73, 139, 140, 141, 205, 219, 230, 272, 277, 296, 297, 331, 335]:
            return StatStageEffect(id, chance)
        else:
            return BannedEffect(id)
