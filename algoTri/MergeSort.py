from random import shuffle
from time import perf_counter
from typing import Any, List

# On définit une fonction MergeSort
# Cet algorithme de tri est recursif, il fait donc appel à lui même dans la définition de sa fonction
# Il fonctionne en séparant la liste en groupes de 1, puis en triant ces groupes pour les joindres à nouveau
# L'un des algorithme les plus rapide, seul probléme, c'est celui qui prend le plus de place sur la RAM pendant son execution
def MergeSort(toSort: List[Any]) -> List[Any]:
    emptyList = []
    # On verifie que la liste d'entrée contient au moins deux éléments
    if len(toSort) > 1:
        # On prend le millieu de la liste, dans le cas d'une taille impaire, la liste de droite sera plus grande
        midPoint = len(toSort) // 2
        # On prend les deux listes correspondants à la séparation en deux, et on les trie avec un MergeSort
        list1, list2 = MergeSort(toSort[:midPoint]), MergeSort(toSort[midPoint:])
        # Les deux listes sont donc maintenant triées indépendamment les unes des autres

        # On inverse les listes, pour avoir les éléments les plus petits à la fin, car ils sont plus rapides à accéder et supprimer
        list1.reverse()
        list2.reverse()
        # On définit des raccourcis aux fonction, car cela rend le code plus rapide à effectuer
        pop1, pop2 = list1.pop, list2.pop

        # On définit une liste vide pour trier les deux listes entre elles
        output = []
        append = output.append
        # Pour tout les éléments des deux listes
        for _ in range(len(list1) + len(list2)):
            # Si la première liste est vide, alors on prend une valeur dans la deuxième
            if list1 == emptyList:
                append(pop2())
            
            # Si la deuxième liste est vide, alors on prend une valeur dans la première
            elif list2 == emptyList:
                append(pop1())

            # Si le dernier élément de la première liste est plus petit que le dernier élément de la deuxième liste
            elif list1[-1] < list2[-1]:
                # Alors on ajoute cette élément à la liste de sortie, et le supprime de sa liste
                append(pop1())
            
            # Sinon, cela signifie que c'est le premier élément de la deuxième liste qui est plus petit
            else:
                # Donc on l'ajoute à la liste de sortie, et le supprime de sa liste
                append(pop2())
        
        # On fini par retourner la liste de sortie
        return output
    
    # Sinon, on retourne l'entrée sans rien faire, afin d'éviter d'avoir une recursion infinie
    return toSort

# On teste la fonction
liste = [*range(100000)]
shuffle(liste)
#print(liste)
t0 = perf_counter()
a = MergeSort(liste)
t1 = perf_counter()
print(t1 - t0)
#print(a)