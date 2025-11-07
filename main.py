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
try:
    event = threading.Event()
    event.clear()

    queue = Queue()

    dish = Dish(functions['ackley'], 5, 20, 10000, event, queue, **ackley_fct_cfg)

    time.sleep(2)

    event.set()

    tstart = time.time()
    while (time.time() - tstart) < 10:
        try:
            data = queue.get()
        except Empty:
            pass

    event.clear()
    print(f"gen : {data['nb_gen']} - SCORE: {data['best_output']} - BEST GENOME {data['best_genome']}")
except KeyboardInterrupt:
    event.clear()
    dish.join()

dish.join()