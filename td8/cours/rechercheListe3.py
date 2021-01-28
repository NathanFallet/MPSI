from typing import Any, List
from time import perf_counter
from random import randint

def contains(l: List[Any], e: Any) -> int:
    d, g = len(l) - 1, 0
    if l[0] > e or l[d] < e:
        return -1
    while g <= d:
        c = (g + d) // 2 
        if l[c] == e:
            return c
        elif l[c] < e:
            g = c + 1
        else:
            d = c - 1
    
    return -1

precision = 10000
liste = [*range(precision)]

t0 = perf_counter()
contains(liste, randint(0, precision-1))
t1 = perf_counter()
print(t1 - t0)