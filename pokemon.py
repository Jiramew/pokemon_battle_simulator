from main.dexLoader import DexLoader
from type import Type
from move import Move
from mechanism.strategy import Strategy


class Pokemon(object):
    def __init__(self, dex=None, pid=None):
        if dex is not None:
            self.dex = dex
        else:
            self.dex = DexLoader().pokedex
        self.pokemon = self.dex.get(str(pid))

        self.name = self.pokemon.get("name")
        self.types = [Type(DexLoader().typedex, type) for type in self.pokemon.get("types")]
        self.weight = self.pokemon.get("weight") / 10

        self.stats = {
            "base": self.pokemon.get("stats"),
            "stage": {
                "attack": 0,
                "defense": 0,
                "spattack": 0,
                "spdefense": 0,
                "speed": 0
            }
        }
        self.maxHp = 141 + 2 * self.pokemon.get("stats").get("hp")
        self.hp = self.maxHp
        self.conditions = []
        self.ailment = None
        self.faintObservers = []
        self.strategy = Strategy(self)
        self.move = None
        self.moves = self.strategy.chooseBuild([Move(mid=move) for move in self.pokemon.get("moves")])
        self.trainer = None
        self.score = 0

    def __str__(self):
        return self.name

    def trainerAndName(self):
        if self.trainer.name is None:
            return "your " + self.name
        else:
            return self.trainer.name + "'s " + self.name

    def stat(self, stat, options=None):
        if options is None:
            options = {}
        if not options.get("ignorePositive"):
            options["ignorePositive"] = False
        if not options.get("ignoreNegative"):
            options["ignoreNegative"] = False

        stageMultiplier = self.statStageMultiplier(self.stats.get("stage").get(stat))

        if (stageMultiplier > 1 and options.get("ingorePositive")) or (
                        stageMultiplier < 1 and options.get("ingoreNegative")):
            stageMultiplier = 1

        ailmentMultiplier = 1
        if self.ailment is not None:
            ailmentMultiplier = self.ailment.statMultiplier(stat)

        return 36 + 2 * self.stats.get("base").get(stat) * stageMultiplier * ailmentMultiplier

    def statStageMultiplier(self, stage):
        if stage == 0:
            return 1
        elif stage > 0:
            return (stage + 2) / 2
        else:
            return 2 / (stage + 2)

    def attack(self):
        return self.stat("attack")

    def defense(self):
        return self.stat("defense")

    def spattack(self):
        return self.stat("spattack")

    def spdefense(self):
        return self.stat("spdefense")

    def speed(self):
        return self.stat("speed")

    def isAlive(self):
        return self.hp > 0

    def chooseMove(self, defender):
        self.move = self.strategy.chooseMove(defender)

    def takeDamage(self, damage, message):
        if damage > self.hp:
            damage = self.hp
        self.hp -= damage
        print(message)
        if not self.isAlive():
            for observer in self.faintObservers:
                observer.notifyFaint(self)

        return damage

    def subscribeToFaint(self, observer):
        self.faintObservers.append(observer)

    def statName(self, stat):
        namedict = {"attack": "Attack", "defense": "Defense", "spattack": "Special Attack",
                    "spdefense": "Special Defense", "speed": "Speed"}

        return namedict.get(stat)

    def modifyStatStage(self, stat, change):
        statName = self.statName(stat)
        if self.stats.get("stage").get(stat) == 6 and change > 0:
            print(self.trainerAndName() + "'s" + statName + " cannot rise any higher.")
        if self.stats.get("stage").get(stat) == -6 and change < 0:
            print(self.trainerAndName() + "'s" + statName + " cannot fall any lower.")
        else:
            change = 6 - self.stats.get("stage").get(stat) if self.stats.get("stage").get(stat) + change > 6 else change
            change = -6 - self.stats.get("stage").get(stat) if self.stats.get("stage").get(
                stat) + change < -6 else change
            self.stats.get("stage")[stat] += change
        if change == 1:
            print(self.trainerAndName() + "'s" + statName + " rose")
        if change == 2:
            print(self.trainerAndName() + "'s" + statName + " sharply rose")
        if change == 3:
            print(self.trainerAndName() + "'s" + statName + " drastically rose")
        if change == -1:
            print(self.trainerAndName() + "'s" + statName + " fell")
        if change == -2:
            print(self.trainerAndName() + "'s" + statName + " harshly fell")
        if change == -3:
            print(self.trainerAndName() + "'s" + statName + " severely fell")

    def typeAdvantageAgainst(self, pokemon):
        type_list = [type for type in self.types if type.effectiveAgainst(pokemon.types)]
        return len(type_list) > 0

    def canAttack(self):
        if self.ailment is not None and not self.ailment.canAttack(self):
            return False
        for x, condition in self.conditions:
            if not condition.canAttack(self):
                return False

        return True

    def whenSwitchedOut(self):
        self.move = None
        if self.ailment is not None:
            self.ailment.whenSwitchedOut(self)
        self.conditions = {}

    def endTurn(self):
        if self.ailment is not None:
            self.ailment.endTurn(self)
        for x, condition in self.conditions:
            condition.endTurn(self)
