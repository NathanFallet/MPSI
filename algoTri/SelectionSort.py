from random import shuffle
from time import perf_counter
from typing import Any, List

# On définit une fonction SelectionSort
# Cet algorithme trouve le minimum de la liste, et le place à la première position, il continue ensuite en ignorant le premier élément
# Cet algorithme, malgrès sa faible efficacité, prend toujours le même temps pour trier une liste de taille n
# L'un des algorithme les plus rapide, seul probléme, c'est celui qui prend le plus de place sur la RAM pendant son execution
def SelectionSort(toSort: List[Any]) -> None:
    # On répéte autant de fois qu'il y a d'éléments dans la liste
    for i in range(len(toSort)):
        # On initialise le minimum de la liste au premier élément étudié
        minimumIndex = i

        # Pour chaque élément de la sous-liste étudiée
        for j in range(i+1, len(toSort)):
            # Si l'élément est plus petit que notre minimum présumé
            if toSort[j] < toSort[minimumIndex]:
                # Alors, c'est notre nouveau minimum présumé
                minimumIndex = j

        # On fini cet itération par échanger le minimum avec le premier élément de la sous-liste étudiée
        toSort[i], toSort[minimumIndex] = toSort[minimumIndex], toSort[i]

# On teste la fonction
liste = [*range(100)]
shuffle(liste)
#print(liste)
t0 = perf_counter()
SelectionSort(liste)
t1 = perf_counter()
print(t1 - t0)
#print(liste)