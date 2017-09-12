from main.dexLoader import DexLoader


class Type(object):
    def __init__(self, dex=None, tid=None):
        if dex is not None:
            self.dex = dex
        else:
            self.dex = DexLoader().typedex

        self.all = list(self.dex.keys())

        if tid is not None:
            self.type = self.dex.get(str(tid))
            self.id = self.type.get("id")
            self.name = self.type.get("name")
            self.offense = self.type.get("offense")
            self.defense = self.type.get("defense")

    def __str__(self):
        return self.name

    @staticmethod
    def all():
        return [Type(tid=typeid) for typeid in DexLoader().typedex.keys()]

    def effectivenessAgainst(self, types):
        if not type(types) == list:
            types = [types]
        base = 1
        for t in types:
            base *= self.offense.get(str(t.id))

        return base

    def effectiveAgainst(self, types):
        return self.effectivenessAgainst(types) > 1

    def weeknesses(self):
        return [Type(self.dex, type_id) for (type_id, effectiveness) in self.defense.items() if effectiveness > 1]

    def strengths(self):
        return [Type(self.dex, type_id) for (type_id, effectiveness) in self.offense.items() if effectiveness > 1]


if __name__ == "__main__":
    dl = DexLoader().typedex
    mv = Type(dl, 12)
    mv.effectiveAgainst([Type(dl, 10), Type(dl, 7)])
