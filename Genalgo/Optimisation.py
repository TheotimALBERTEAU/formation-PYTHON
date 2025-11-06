from Genalgo.Classes.Cell import Cell

def Optimisation():
    all_cells = []
    PCT_BEST = 20
    NCELL = 100

    for _ in range(NCELL):
        all_cells.append(Cell())

    gen = 0
    while True:
        for cell in all_cells:
            cell.apply()

        trie = sorted(all_cells, key=lambda inp: inp.output)
        print(f"GEN {gen} SCORE {trie[0].output} GENOME {trie[0].genome}")

        ncut = NCELL * (PCT_BEST / 100)

        all_cells = trie[:int(ncut)]

        parent = 0
        while len(all_cells) < NCELL:
            cellule_parent = all_cells[parent]
            parent += 1
            if parent >= ncut:
                parent = 0
            child = cellule_parent.child()
            all_cells.append(child)

        gen += 1
        assert len(all_cells) == NCELL