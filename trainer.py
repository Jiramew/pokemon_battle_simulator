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
        if random.random() < 0.67:
            return own
        if not opponent.typeAdvantageAgainst(own):
            return own
        if len([pokemon for pokemon in self.ablePokemon() if not opponent.typeAdvantageAgainst(own)]) > 0:
            return own
        print("withdrew " + own + ".")
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

        print("took out" + self.mainPokemon)
        return self.mainPokemon

    def nameOrYou(self):
        return self.name if self.name else "you"
