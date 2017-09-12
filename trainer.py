import random


class Trainer(object):
    def __init__(self, name):
        self.name = name
        self.team = []
        self.mainPokemon = None

    def addPokemon(self, pokemon):
        pokemon.trainer = self
        self.team.append(pokemon)

    def ablePokemon(self):
        return [pokemon for pokemon in self.team if pokemon.isAlive()]

    def firstPokemon(self):
        self.mainPokemon = self.team[0]

    def maybeSwitchOut(self, own, opponent):
        score = 0
        if not len([pokemon for pokemon in self.ablePokemon() if not opponent.typeAdvantageAgainst(pokemon)]) > 0:
            return own
        else:
            score += 5

        if not opponent.typeAdvantageAgainst(own):
            return own
        else:
            score += 3

        if not score >= 5:
            if random.random() < 0.5:
                return own
        else:
            print("withdrew " + str(own) + ".")
            self.switchPokemon(opponent)
            return self.mainPokemon

    def switchPokemon(self, opponent):
        self.mainPokemon.stats["stage"] = {
            "attack": 0,
            "defense": 0,
            "spattack": 0,
            "spdefense": 0,
            "speed": 0
        }
        candidates = [pokemon for pokemon in self.ablePokemon() if pokemon != self.mainPokemon]
        maxScore = -1
        for pokemon in candidates:
            if pokemon.typeAdvantageAgainst(opponent):
                pokemon.score += 1
            if opponent.typeAdvantageAgainst(pokemon):
                pokemon.score -= 1
            if pokemon.score > maxScore:
                maxScore = pokemon.score

        bestChoices = [pokemon for pokemon in candidates if pokemon.score == maxScore]
        self.mainPokemon = random.sample(bestChoices, 1)[0]
        if self.mainPokemon is not None:
            self.mainPokemon.whenSwitchedOut()

        print("took out" + self.mainPokemon.name)
        return self.mainPokemon

    def nameOrYou(self):
        return self.name if self.name else "you"
