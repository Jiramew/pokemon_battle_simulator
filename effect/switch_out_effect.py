from effect.default_effect import DefaultEffect


class SwitchOutEffect(DefaultEffect):
    def __init__(self, id, chance=None):
        super(SwitchOutEffect, self).__init__(id, chance)

    def battleMultiplier(self, attacker, defender, damage, lethal):
        has_other_pokemon = attacker.train.ablePokemon().length > 1
        if defender.typeAdvantageAgainst(attacker) and attacker.spped() > defender.speed() and has_other_pokemon:
            return 2
        else:
            return 1

    def afterDamage(self, attacker, defender, damage):
        trainer = attacker.trainer
        if trainer.ablePokemon().length > 1:
            trainer.switchPokemon(defender)
