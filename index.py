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
    team1 = {trainer}


if __name__ == '__main__':
    pokemon = {}
    print(pokemon_lookup("arcanine"))
