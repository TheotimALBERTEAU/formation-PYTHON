#-*-encoding:utf-8*-

NDIM=5
XMIN=-4
XMAX=4
YMIN=0
XOPTI=0

PCT_BEST = 35
NCELL = 10000

import random
import math

def sphere(inputs):
    s = 0
    for x in inputs:
        s += x ** 2
    return s

def salomon(inputs):
    s = 0
    for x in inputs:
        s += x ** 2
    u = math.pi * 2 * math.sqrt(s)
    res = 1 - math.cos(u) + 0.1 * math.sqrt(s)
    return res

assert salomon([XOPTI, XOPTI]) == YMIN
assert salomon([XMIN, XMAX]) > YMIN
assert salomon([XMAX, XMIN]) > YMIN

def conversion(gene):
    # b = XMIN
    # A = XMAX - XMIN
    return (XMAX - XMIN) * gene + XMIN 

assert conversion(0.0) == XMIN
assert conversion(1.0) == XMAX
assert conversion(0.5) == XOPTI

def trad(genome):    # Liste de gènes
    inputs = []
    for gene in genome:
        inputs.append(conversion(gene))
    return inputs
    
assert trad([1.0, 0.0, 0.5]) == [XMAX, XMIN, XOPTI]

class Cellule:
    def __init__(self):
        self.genome = []
        for _ in range(0, NDIM):
            self.genome.append(random.random())

    def apply(self):
        inputs = trad(self.genome)
        # self.output = salomon(inputs)
        self.output = sphere(inputs)

    def reset(self):
        self.output = None

    def child(self):
        enfant = Cellule()
        enfant.genome = self.genome.copy()
        n = random.randrange(0, len(enfant.genome))
        enfant.genome[n] = random.random()
        return enfant

def opti():
    # Initialisation
    cellules = []
    for _ in range(NCELL):
        cellules.append(Cellule())

    nbgeneration = 0
    while True:
        # Pour chaque génération:
        for cell in cellules:
            cell.apply()
        # On sélectionne les meilleures cellules
        trie = sorted(cellules, key = lambda inp: inp.output)
        print("GEN", nbgeneration, "SCORE", trie[0].output, "GENOME", trie[0].genome)
        # On calcule combien de cellules on garde (X% meilleures)
        ncut = NCELL * (PCT_BEST / 100)
        print(ncut)

        # On supprime toutes les autres cellules (pas dans les X% meilleures)
        cellules = trie[:int(ncut)]
        parent = 0
        while len(cellules) < NCELL:
            # On complète la génération par des enfants
            cellule_parent = cellules[parent]
            parent += 1    # L'index du parent qu'on sélectionne pour créer l'enfant
            if parent >= ncut:
                parent = 0
            enfant = cellule_parent.child()    # On créé l'enfant
            cellules.append(enfant)    # On ajoute à la liste des cellules (pour la next gen)

        # Et z'est repartiiiiiiiiii
        nbgeneration += 1
        assert len(cellules) == NCELL

opti()
