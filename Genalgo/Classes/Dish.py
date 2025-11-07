import time
from Genalgo.Classes.Cell import Cell
from threading import Thread
from queue import Queue, Empty

class Dish(Thread):
    def __init__(self, fonction, ndim, pct_best, ncell, event, queue : Queue, **fct_cfg):

        super().__init__()

        self.fonction = fonction
        self.NDIM = ndim
        self.PCT_BEST = pct_best
        self.NCELL = ncell
        self.Event = event
        self.Queue = queue
        self.fct_cfg = fct_cfg

        self.gen = 0
        self.all_cells = []

        for _ in range(self.NCELL):
            self.all_cells.append(Cell(self.fonction, self.NDIM, **self.fct_cfg))

        self.start()

    def new_gen(self):
        for cell in self.all_cells:
            cell.apply()

        trie = sorted(self.all_cells, key=lambda inp: inp.output)

        best_cell = trie[0]
        data = {
            'nb_gen': self.gen,
            'best_output' : best_cell.output,
            'best_genome' : best_cell.genome,
        }

        self.Queue.put(data)

        ncut = self.NCELL * (self.PCT_BEST / 100)

        self.all_cells = trie[:int(ncut)]

        parent = 0
        while len(self.all_cells) < self.NCELL:
            cellule_parent = self.all_cells[parent]
            parent += 1
            if parent >= ncut:
                parent = 0
            child = cellule_parent.child()
            self.all_cells.append(child)


        self.gen += 1
        assert len(self.all_cells) == self.NCELL

    def run(self):
        print("Init Dish")
        self.Event.wait()

        print("Event set, Simulation Start")
        while self.Event.is_set():
            self.new_gen()

        print("Arret de Dish")