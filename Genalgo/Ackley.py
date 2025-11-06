from Genalgo.Decorators.InputTranslate import input_translate
import math

@input_translate
def ackley(n, **fct_cfg):
    S = 0
    for x in range(len(n)):
        S += n[x] ** 2
    S = 1/len(n) * S
    T = 0
    for x in range(len(n)):
        T += math.cos(fct_cfg['c']*n[x])
    T = 1/len(n) * T

    U = -fct_cfg['a'] * math.exp(-fct_cfg['b'] * math.sqrt(S)) - math.exp(T) + fct_cfg['a'] + math.exp(1)
    return U