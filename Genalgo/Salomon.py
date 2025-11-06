import math

def salomon(inputs, **fct_cfg):
    s = 0
    for x in inputs:
        s += x ** 2
    u = fct_cfg['c'] * math.sqrt(s)
    res = fct_cfg['a'] - math.cos(u) + fct_cfg['b'] * math.sqrt(s)
    return res