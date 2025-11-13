import math
import threading
import time
from Functions.Fibonacci import Fibonacci
from Functions.Calculator import Calculator
from Functions.Pendu import Pendu
from Functions.MatchPattern import MatchPattern
from Functions.Luhn import Luhn
from Functions.BubbleSort import BubbleSort
from Functions.FusionSort import FusionSort
from Genalgo.Sphere import sphere
from Genalgo.Translate import translate
from Genalgo.Optimisation import optimisation
from Genalgo.Decorators.InputTranslate import input_translate
from Genalgo.Salomon import salomon
from Genalgo.Ackley import ackley
from Genalgo.Classes.Dish import Dish
from queue import Queue, Empty
import multiprocessing
from multiprocessing import Process, Event, Queue # Modifier les imports
from multiprocessing import Process, Event, Queue
from concurrent.futures import ThreadPoolExecutor

# <editor-fold desc="Test des fonctions">
# print(Fibonacci(10))
#print(Calculator("32 + 5"))
# Pendu('anticonstitutionnelemental')
# print(MatchPattern("AABAACAADAABAABA", "AABA"))
# print(Luhn("4539 7043 5470 6091"))
# </editor-fold>

# <editor-fold desc="Création des listes">
non_trie = [4, 42, 13, 26, 27, 16, 32, 37, 43, 17, 49, 6, 25, 5, 38, 48, 35, 40, 7, 31, 10, 18,
41, 21, 19, 28, 30, 12, 33, 36, 47, 24, 29, 2, 0, 9, 15, 11, 14, 3, 23, 20, 8, 44, 39, 34, 46,
45, 22, 1]
trie = list(range(-40, 41))
# </editor-fold>

functions = {
    'ackley' : ackley,
    'salomon' : salomon,
}

ackley_fct_cfg = {
    'a' : 20,
    'b' : 0.2,
    'c' : 2 * math.pi,
    'higher' : 40,
    'lower' : -40
}

salomon_fct_cfg = {
    'a': 1,
    'b': 0.1,
    'c': 2 * math.pi,
    'higher': 5,
    'lower': -5
}

configurations = [
    {'fonction': functions['ackley'], 'ndim': 3, 'pct_best': 30, 'ncell': 500, 'cfg': ackley_fct_cfg,
     'name': 'Ackley_Slow'},

    {'fonction': functions['salomon'], 'ndim': 10, 'pct_best': 20, 'ncell': 5000, 'cfg': salomon_fct_cfg,
     'name': 'Salomon'},

    {'fonction': functions['ackley'], 'ndim': 5, 'pct_best': 20, 'ncell': 1000, 'cfg': ackley_fct_cfg,
     'name': 'Ackley_Fast'},
]

duree_exec = 60
event = multiprocessing.Event()
event.clear()

dishes = []
queues = []

try:
    print("Prepa dishs")
    for i, cfg in enumerate(configurations):
        queue = multiprocessing.Queue()
        queues.append(queue)

        dish = Dish(
            cfg['fonction'],
            cfg['ndim'],
            cfg['pct_best'],
            cfg['ncell'],
            event,
            queue,
            **cfg['cfg'],
        )
        dishes.append(dish)
        print(f"[{cfg['name']}] prêt. NDIM={cfg['ndim']}, NCELL={cfg['ncell']}")

    print("Demarrage threads")
    for dish in dishes:
        dish.start()

    time.sleep(2)
    event.set()
    print("Lancement des simus")

    tstart = time.time()
    while (time.time() - tstart) < duree_exec:
        for i, q in enumerate(queues):
            try:
                data = q.get(timeout=0.1)
                name = configurations[i]['name']
                print(f"[RES - {name}] Gen: {data['nb_gen']} | Score: {data['best_output']}")

            except Empty:
                pass
    event.clear()
except KeyboardInterrupt:
    event.clear()

finally:
    for dish in dishes:
        if dish.is_alive():
            dish.join()
    print("Fermeture des threads")