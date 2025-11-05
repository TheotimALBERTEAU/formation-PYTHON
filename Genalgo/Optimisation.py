from Genalgo.Classes.Cell import Cell
import random

plage = list(range(0, 41))

def Optimisation(N):
    gen = 0
    NDIM = 1000
    all_cells = []
    best_cell = Cell(list(random.random() for _ in range(NDIM)), NDIM, plage)
    best_cell.apply()

    for i in range(N):
        gen += 1
        cell = Cell(list(random.random() for _ in range(NDIM)), NDIM, plage)
        cell.apply()
        cell.genome.sort()

        all_cells.append(cell)

        if cell.output < best_cell.output:
            best_cell = cell
            best_cell.output = cell.output

        print(f"GENERATION {gen}, MINIMUM : {all_cells[0].output}, MEILLEUR GENOME : {best_cell.genome}")


    all_cells = sorted(all_cells, key=lambda c: c.genome)
    all_cells[:int(N * 0.2)]

    while len(all_cells) < N:
        all_cells.append(best_cell.child())
