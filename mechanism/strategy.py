from mechanism.damage_calculator import DamageCalculator
from type import Type
from move import Move
from move import struggle


class Strategy(object):
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.helpfulTypes = []
        for weekness in [type for type in Type.all() if type.effectiveAgainst(self.pokemon.types)]:
            self.helpfulTypes.extend([type.id for type in Type.all() if type.effectiveAgainst(weekness)])

    def chooseBuild(self, moves):
        scoredMoves = []
        for move in moves:
            if move.banned():
                continue
            else:
                scoredMove = self.scoreMoveForBuild(move)
                scoredMoves.append(scoredMove)
        scoredMoves = sorted(scoredMoves, key=lambda x: -x['score'])

        chosenMoves = []
        typesCovered = []
        for move in scoredMoves:
            if move.get("move").type.id not in typesCovered:
                chosenMoves.append(move.get("move"))
                typesCovered.append(move.get("move").type.id)
                if len(typesCovered) == 4:
                    break
            if len(chosenMoves) == 0:
                chosenMoves = [struggle]

        return chosenMoves

    def scoreMoveForBuild(self, move):
        if move.type.id in [type.id for type in self.pokemon.types]:
            typeMultiplier = 1.5
        elif move.type.id in self.helpfulTypes:
            typeMultiplier = 1.2
        elif len(move.type.strengths()) in [0, 1, 2]:
            typeMultiplier = 0.9
        elif len(move.type.strengths()) == 3:
            typeMultiplier = 1
        else:
            typeMultiplier = 1.1

        stat = self.pokemon.stat(move.attackStat())
        return {"move": move,
                "score": move.power() * typeMultiplier * stat * move.accuracy * move.buildMultiplier(self.pokemon)}

    def chooseMove(self, defender):
        damageCalculator = DamageCalculator()

        bestMove = None
        bestDamage = -1
        for move in self.pokemon.moves:
            damage = damageCalculator.calculate(move, self.pokemon, defender)
            damage = defender.hp if defender.hp < damage else damage
            damage *= move.battleMultiplier(self.pokemon, defender, damage)

            if damage > bestDamage:
                bestMove = move
                bestDamage = damage

        self.pokemon.move = bestMove
        return bestMove
