from typing import Any, List, Tuple
from time import perf_counter
from random import randint, shuffle

def contains(l: List[Any], e: Any) -> Tuple[bool, int]:
    n, found, index = len(l), False, -1
    for i in range(n-1):
        if l[i] == e:
            found, index = True, i
    
    return found, index

precision = 10000
liste = [*range(precision)]
shuffle(liste)

t0 = perf_counter()
contains(liste, randint(0, precision-1))
t1 = perf_counter()
print(t1 - t0)