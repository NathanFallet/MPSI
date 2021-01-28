from typing import Any, List
from time import perf_counter
from random import randint, shuffle

def contains(l: List[Any], e: Any) -> bool:
    i = 0
    while i < len(l) and l[i] != e:
        i = i + 1
    
    if i < len(l):
        return True
    else:
        return False

precision = 10000
liste = [*range(precision)]
shuffle(liste)

t0 = perf_counter()
contains(liste, randint(0, precision-1))
t1 = perf_counter()
print(t1 - t0)