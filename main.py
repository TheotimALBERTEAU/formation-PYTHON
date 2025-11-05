from Functions.Fibonacci import Fibonacci
from Functions.Calculator import Calculator
from Functions.Pendu import Pendu
from Functions.MatchPattern import MatchPattern
from Functions.Luhn import Luhn
from Functions.BubbleSort import BubbleSort
from Functions.FusionSort import FusionSort
from Genalgo.Sphere import Sphere
from Genalgo.Translate import Translate
from Genalgo.Optimisation import Optimisation

# print(Fibonacci(10))
#print(Calculator("32 + 5"))
# Pendu('anticonstitutionnelemental')
# print(MatchPattern("AABAACAADAABAABA", "AABA"))
# print(Luhn("4539 7043 5470 6091"))

non_trie = [4, 42, 13, 26, 27, 16, 32, 37, 43, 17, 49, 6, 25, 5, 38, 48, 35, 40, 7, 31, 10, 18,
41, 21, 19, 28, 30, 12, 33, 36, 47, 24, 29, 2, 0, 9, 15, 11, 14, 3, 23, 20, 8, 44, 39, 34, 46,
45, 22, 1]
trie = list(range(-40, 41))
translated_list = list(range(Translate(trie, 0), Translate(trie, 1) + 1))
# print(FusionSort(non_trie))

Optimisation(10000000)