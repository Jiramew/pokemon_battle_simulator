from main.dexLoader import DexLoader

DAMAGE_NONE = "non-damaging"
DAMAGE_PHYSICAL = 'physical'
DAMAGE_SPECIAL = 'special'


class Move(object):
    def __init__(self, dex, mid):
        self.dex = dex
        self.struggle = Move(dex, 165)
        self.move = self.dex.get(str(mid))



if __name__ == "__main__":
    pass
