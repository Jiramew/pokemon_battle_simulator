import json


class DexLoader(object):
    def __init__(self):
        with open("data/pokemons.json", encoding="utf-8") as f_poke:
            self.pokedex = json.loads(f_poke.read().strip())
        with open("data/moves.json", encoding="utf-8") as f_move:
            self.movedex = json.loads(f_move.read().strip())
        with open("data/types.json", encoding="utf-8") as f_type:
            self.typedex = json.loads(f_type.read().strip())


if __name__ == "__main__":
    dl = DexLoader()
