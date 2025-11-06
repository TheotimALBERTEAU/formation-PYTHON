from Genalgo.Translate import Translate
from Genalgo.Ackley import Ackley
import copy, random

class Cell:
    def __init__(self):
        self.NDIM = 10
        self.genome = list(random.random() for _ in range(self.NDIM))
        self.output = []

    def trad(self, genome):
        inputs = []
        for gene in self.genome:
            inputs.append(Translate(self.genome, gene))
        return inputs

    def apply(self):
        # inputs = self.trad(self.genome)
        self.output = Ackley(self.genome)

    def child(self):
        enfant = Cell()
        enfant.genome = self.genome.copy()
        n = random.randrange(0, len(enfant.genome))
        enfant.genome[n] = random.random()
        return enfant

    def reset(self):
        self.output = []