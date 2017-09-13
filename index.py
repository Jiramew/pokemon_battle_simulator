from main.dexLoader import DexLoader
from pokemon import Pokemon
from trainer import Trainer
from battle import Battle

dl = DexLoader()


def pokemon_lookup(name):
    name = name.lower()
    if name == "nidoran f":
        return 29
    elif name == "nidoran m":
        return 32
    else:
        pkdex = dl.pokedex
        return [v.get("id") for k, v in pkdex.items() if v.get("name").lower() == name][0]


def pokemon_battle(team1, team2):
    team1 = {"trainer": None, "pokemon": team1}
    team2 = {"trainer": "The foe", "pokemon": team2}

    trainer1 = Trainer(team1.get("trainer"))
    for pkm in team1.get("pokemon"):
        trainer1.addPokemon(Pokemon(pid=pkm))
    trainer2 = Trainer(team2.get("trainer"))
    for pkm in team2.get("pokemon"):
        trainer2.addPokemon(Pokemon(pid=pkm))

    print(trainer1.nameOrYou() + " took out " + " ".join([pokemon.name for pokemon in trainer1.team]))
    print(trainer2.nameOrYou() + " took out " + " ".join([pokemon.name for pokemon in trainer2.team]))
    print("\n")

    battle = Battle(trainer1, trainer2)
    return battle.start()


def pokemon_build(pokemonId):
    pokemon = Pokemon(pid=pokemonId)
    return "\n".join([str(move) for move in pokemon.moves])


if __name__ == '__main__':
    pokemon_battle([143, 144, 145, 146], [151, 148, 149, 150])
# pokemon = {}
# print(pokemon_lookup("arcanine"))
