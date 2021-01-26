from typing import Any, List
from time import perf_counter_ns
from random import randint

def maxList(l: List[Any]) -> Any:
    t0 = perf_counter_ns()
    m = l[0]
    for i in range(len(l)):
        if l[i] > m:
            m = l[i]
    t1 = perf_counter_ns()
    return t1 - t0

liste = [randint(1, 100) for i in range(10)]

print(maxList(liste))