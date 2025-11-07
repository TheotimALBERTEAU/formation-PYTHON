#-*-encoding:utf-8*-

YMIN=0
XOPTI=0

import random
import math

def conversion(gene, higher, lower):
    res = (higher - lower) * gene + lower
    return res

assert conversion(0.0, 10, -10) == -10
assert conversion(1.0, 10, -10) == 10
assert conversion(0.5, 10, -10) == 0

def trad(genome, higher, lower):
    inputs = []
    for gene in genome:
        inputs.append(conversion(gene, higher, lower))
    return inputs
    
assert trad([1.0, 0.0, 0.5], 10, -10) == [10, -10, 0]

def input_traduction(f):
    def decorated(genome, higher=10, lower=-10, **fct_cfg):
        inputs = trad(genome, higher, lower)
        return f(inputs, **fct_cfg)
    return decorated

@input_traduction
def sphere(inputs, **kwargs):
    s = 0
    for x in inputs:
        s += x ** 2
    return s

@input_traduction
def salomon(inputs, k=2*math.pi, **kwargs):
    s = 0
    for x in inputs:
        s += x ** 2
    u = k * math.sqrt(s)
    res = 1 - math.cos(u) + 0.1 * math.sqrt(s)
    return res

assert salomon([0.5, 0.5]) == YMIN
assert salomon([0.0, 1.0]) > YMIN
assert salomon([1.0, 0.0]) > YMIN

FCTS = {
    "salomon": salomon,
    "sphere": sphere,
}

class Cellule:
    def __init__(self, name, fct_cfg, ndim=5):
        self.name = name
        self.ndim = ndim
        self.f = FCTS[name]
        self.fct_cfg = fct_cfg
        self.genome = []
        for _ in range(0, ndim):
            self.genome.append(random.random())

    def apply(self):
        self.output = self.f(self.genome, **self.fct_cfg)

    def reset(self):
        self.output = None

    def child(self):
        enfant = Cellule(self.name, self.fct_cfg, ndim=self.ndim)
        enfant.genome = self.genome.copy()
        n = random.randrange(0, len(enfant.genome))
        enfant.genome[n] = random.random()
        return enfant

def main(name, ncell=1000, pct_best=35, ndim=5, **fct_cfg):
    # Initialisation
    cellules = []
    for _ in range(ncell):
        cellules.append(Cellule(name, fct_cfg, ndim=ndim))

    nbgeneration = 0
    while True:
        # Pour chaque génération:
        for cell in cellules:
            cell.apply()
        # On sélectionne les meilleures cellules
        trie = sorted(cellules, key = lambda inp: inp.output)
        print("GEN", nbgeneration, "SCORE", trie[0].output / ndim, "GENOME", trie[0].genome)
        # On calcule combien de cellules on garde (X% meilleures)
        ncut = ncell * (pct_best / 100)

        # On supprime toutes les autres cellules (pas dans les X% meilleures)
        cellules = trie[:int(ncut)]
        parent = 0
        while len(cellules) < ncell:
            # On complète la génération par des enfants
            cellule_parent = cellules[parent]
            parent += 1    # L'index du parent qu'on sélectionne pour créer l'enfant
            if parent >= ncut:
                parent = 0
            enfant = cellule_parent.child()    # On créé l'enfant
            cellules.append(enfant)    # On ajoute à la liste des cellules (pour la next gen)

        # Et z'est repartiiiiiiiiii
        nbgeneration += 1
        assert len(cellules) == ncell

main("salomon", ndim=50, ncell=30000, pct_best=50)
