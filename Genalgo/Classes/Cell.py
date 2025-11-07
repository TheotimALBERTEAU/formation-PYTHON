import copy, random

class Cell:
    def __init__(self, fonction, ndim, **fct_cfg):
        self.NDIM = ndim
        self.genome = list(random.random() for _ in range(self.NDIM))
        self.output = []
        self.fonction = fonction
        self.fct_cfg = fct_cfg

    def apply(self):
        self.output = self.fonction(self.genome, **self.fct_cfg)

    def child(self):
        enfant = Cell(self.fonction, self.NDIM, **self.fct_cfg)
        enfant.genome = self.genome.copy()
        n = random.randrange(0, len(enfant.genome))
        enfant.genome[n] = random.random()
        return enfant

    def reset(self):
        self.output = []