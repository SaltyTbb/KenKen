import math
class Level(object):
    rules={}
    cells=""
    size=0

    def __init__(self,rules,cells):
        self.rules=rules
        self.cells=cells
        self.size=int(math.sqrt(len(cells)))