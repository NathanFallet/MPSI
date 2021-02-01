from typing import Any, List
from random import shuffle
from time import perf_counter

# Fonction auxiliaire calculant le median des valeurs de trois indices dans une liste
def medOfThree(list: List[Any], low: int, mid: int, high: int):
    if list[mid] < list[low]:
        mid, low = low, mid
    if list[high] < list[low]:
        high, low = low, high
    if list[mid] < list[high]:
        mid, high = high, mid
    return high


# On définit une fonction QuickSort
# C'est un algorithme de tri récursif, qui divise la liste en sous-liste pour faciliter le tri
# Il commence par prendre un pivot, ici il prend le ninther, qui est une approximation du médian
# Ensuite, il sépare la liste en deux: d'un côté les éléments plus petits ou égals au pivot, et les éléments plus grands
# Il s'appelle ensuite sur chacune des deux sous-listes, puis les joint ensemble
# Si l'implémentation est efficace, c'est le plus rapide de tous les algorithmes, mais il a beaucoup de problèmes à trier des listes avec des éléments identiques
def QuickSort(toSort: List[Any]) -> List[Any]:
    # On prend la longueur de toSort, pour ne pas avoir à la recalculer à chaque fois
    n = len(toSort)
    # Si la liste a au moins 4 éléments
    if n > 3:
        # On calcule les positions importantes de nos trois sous-listes
        low1, med1, high1, med2, high2, med3, high3 = 0, n // 6, (2 * n) // 6, (3 * n) // 6, (4 * n) // 6, (5 * n) // 6, n-1
        # On calcule le ninther, soit la médiane des trois médianes de chaque tiers de liste, et on s'en sert pour choisir notre pivot
        pivot = toSort[medOfThree(toSort, medOfThree(toSort, low1, med1, high1), medOfThree(toSort, high1+1, med2, high2), medOfThree(toSort, high2+1, med3, high3))]
        
        # On définit deux liste vides
        lList, rList = [], []
        # Et on assigne les fonctions à des variables, car c'est plus rapide à éxécuter
        append1, append2 = lList.append, rList.append

        # Pour chaque élément de la liste
        for i in toSort:
            # Si il est plus grand que le pivot, alors il va à droite
            if i > pivot:
                append2(i)
            # Sinon, il va à gauche
            else:
                append1(i)

        return QuickSort(lList) + QuickSort(rList)
    
    # On gère le cas à deux éléments
    if n == 3:
        # Si le deuxième élément et plus petit que le premier
        if toSort[0] > toSort[1]:
            # On les change de place
            toSort[0], toSort[1] = toSort[1], toSort[0]
        # Si le troisième élément et plus petit que le deuxième
        if toSort[1] > toSort[2]:
            # On les change de place
            toSort[1], toSort[2] = toSort[2], toSort[1]
        # Si le deuxième élément et plus petit que le premier
        if toSort[0] > toSort[1]:
            # On les change de place
            toSort[0], toSort[1] = toSort[1], toSort[0]

    # On gère le cas à deux éléments
    elif n == 2:
        # Si le deuxième élément et plus petit que le premier
        if toSort[1] < toSort[0]:
            # On les change de place
            toSort[0], toSort[1] = toSort[1], toSort[0]
    
    # On retourne la liste, pour les cas à 0, 1, 2 et 3 éléments
    return toSort

# On teste la fonction
liste = [*range(100)]
shuffle(liste)
# print(liste)
t0 = perf_counter()
a = QuickSort(liste)
t1 = perf_counter()
print(t1 - t0)
#print(a)