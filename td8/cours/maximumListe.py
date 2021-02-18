from typing import Any, List
from time import perf_counter
from random import shuffle

def maxList(l: List[Any]) -> Any:
    m = l[0]
    for i in range(len(l)):
        if l[i] > m:
            m = l[i]
    return m

liste = [*range(100)]
shuffle(liste)

t0 = perf_counter()
maxList(liste)
t1 = perf_counter()
print(t1 - t0)