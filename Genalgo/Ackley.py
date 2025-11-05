import math

def Ackley(n):
    S = 0
    for x in range(len(n)):
        S += n[x] ** 2
    S = 1/len(n) * S
    T = 0
    for x in range(len(n)):
        T += math.cos((2*math.pi)*n[x])
    T = 1/len(n) * T

    U = -20 * math.exp(-0.2 * math.sqrt(S)) - math.exp(T) + 20 + math.exp(1)
    return U