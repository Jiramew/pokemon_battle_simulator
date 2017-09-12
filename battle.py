import random
from type import Type
from move import Move
from pokemon import Pokemon
from mechanism.damage_calculator import DamageCalculator


class Battle(object):
    def __init__(self, trainer1, trainer2):
        self.winner = None
        self.stopMultiHit = None
        self.trainer1 = trainer1
        self.trainer2 = trainer2
        self.damageCalculator = DamageCalculator()

        self.trainer1.firstPokemon()
        self.trainer2.firstPokemon()
        for pokemon in trainer1.team:
            pokemon.subscribeToFaint(self)
        for pokemon in trainer2.team:
            pokemon.subscribeToFaint(self)

    def start(self):
        while not self.winner:
            self.nextTurn()
            print("")

        loser = self.trainer1 if self.winner == self.trainer2 else self.trainer2
        print(self.winner.nameOrYou() + " defeated " + loser.nameOrYou() + "!")
        for pokemon in self.winner.team:
            print(
                pokemon.name + ": " + str(pokemon.hp) + " HP (" + str(
                    round(pokemon.hp / pokemon.maxHp * 100)) + "%) left.")

    def nextTurn(self):
        pokemon1 = self.trainer1.mainPokemon
        pokemon2 = self.trainer2.mainPokemon

        pokemon1.chooseMove(pokemon2)
        pokemon2.chooseMove(pokemon1)

        newPokemon1 = pokemon1.trainer.maybeSwitchOut(pokemon1, pokemon2)
        newPokemon2 = pokemon2.trainer.maybeSwitchOut(pokemon2, pokemon1)
        pokemon1 = newPokemon1
        pokemon2 = newPokemon2

        if not (pokemon1.move and pokemon2.move):
            pkmn1GoseFirst = True
        elif pokemon1.move.priority == pokemon2.move.priority:
            pkmn1GoseFirst = (pokemon1.speed() > pokemon2.speed()) or (
                pokemon1.speed() == pokemon2.speed() and random.random() < 0.5)
        else:
            pkmn1GoseFirst = pokemon1.move.priority > pokemon2.move.priority

        if pkmn1GoseFirst:
            attacker = pokemon1
            defender = pokemon2
        else:
            attacker = pokemon2
            defender = pokemon1
        if attacker.move is not None:
            self.doAttack(attacker, defender)

        attacker = attacker.trainer.mainPokemon
        defender = defender.trainer.mainPokemon

        if defender.move is not None and not self.winner:
            self.doAttack(defender, attacker)

        if attacker.isAlive() and not self.winner:
            attacker.endTurn()
        if defender.isAlive() and not self.winner:
            defender.endTurn()

    def criticalChance(self, stage):
        if stage == 0:
            return 1 / 16
        elif stage == 1:
            return 1 / 8
        elif stage == 2:
            return 1 / 2
        else:
            return 1

    def doAttack(self, attacker, defender):
        if attacker.canAttack():
            print(attacker.trainerAndName() + " used " + attacker.move.name + "!")
            effectiveness = attacker.move.effectiveness(attacker, defender)
            miss = False
            if effectiveness == 0:
                print("It dosen't affect " + defender.trainerAndName() + "...")
                miss = True
            else:
                if random.random() * 100 > attacker.move.accuracy:
                    print(attacker.trainerAndName() + "'s attack missed")
                    miss = True
                else:
                    hits = attacker.move.hits()
                    hit = 0
                    miss = False
                    self.stopMultiHit = False
                    while not ((hit == hits) or self.stopMultiHit):
                        hit += 1
                        critical = random.random() < self.criticalChance(attacker.move.criticalRateStage())
                        rand = random.random() * (1 - 0.85 + 0.85)
                        if critical:
                            print("It's a critical hit!")
                        if effectiveness > 1:
                            print("It's super effective!")
                        if effectiveness < 1:
                            print("It's not very effective...")
                        damage = self.damageCalculator.calculate(attacker.move, attacker, defender, critical, rand)
                        defender.takeDamage(damage, "{0} was hit for {1}".format(defender.name, damage))
                        attacker.move.afterDamage(attacker, defender, damage)
                if miss:
                    attacker.move.afterMiss(attacker, defender)

    def notifyFaint(self, pokemon):
        print(pokemon.trainerAndName() + " fainted!")
        self.stopMultiHit = True

        otherTrainer = self.trainer1 if pokemon.trainer == self.trainer2 else self.trainer2
        if len(pokemon.trainer.ablePokemon()) == 0:
            if not self.winner:
                self.winner = otherTrainer
        if not self.winner:
            pokemon.trainer.switchPokemon(otherTrainer.mainPokemon)
