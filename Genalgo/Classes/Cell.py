from Genalgo.Translate import Translate
from Genalgo.Ackley import Ackley
import copy, random

class Cell:
    def __init__(self, genome : list, NDIM, plage_valeurs):
        self.genome = genome
        self.output = []
        self.NDIM = NDIM
        self.plage_valeurs = plage_valeurs

    def apply(self):
        translated_genome = []
        for i in self.genome:
            translated_genome.append(Translate(self.plage_valeurs, i))
        self.output = (Ackley(translated_genome))
        return self.output

    def child(self):
        clone = copy.deepcopy(self)
        clone.genome[random.randrange(0, len(clone.genome))] = random.random()
        clone.reset()

    def reset(self):
        self.output = []