from typing import Any, List
from random import shuffle

def QuickSort(toSort: List[Any]) -> Any:
    if len(toSort) > 1:
        n = len(toSort)
        def medOfThree(list, low, mid, high):
            if list[mid] < list[low]:
                mid, low = low, mid
            if list[high] < list[low]:
                high, low = low, high
            if list[mid] < list[high]:
                mid, high = high, mid
            return high
        low1, med1, high1, med2, high2, med3, high3 = 0, n // 6, (2 * n) // 6, (3 * n) // 6, (4 * n) // 6, (5 * n) // 6, n-1
        pivot = medOfThree(toSort, medOfThree(toSort, low1, med1, high1), medOfThree(toSort, high1+1, med2, high2), medOfThree(toSort, high2+1, med3, high3))
        

a = [*range(100)]
shuffle(a)
print(QuickSort(a))