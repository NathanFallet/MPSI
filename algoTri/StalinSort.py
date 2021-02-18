from random import shuffle
from typing import Any, List

# On définit une fonction StalinSort
# Cet algorithme fonctionne en supprimant tout les éléments non conformes (d'où le nom).
# Ceci n'est pas un véritable alogrithme de tri, car l'intégrité de la liste n'est pas conservée. C'est purement une blague.
def StalinSort(toSort: List[Any]) -> None:
    # On initialise la valeur précédente à 0, car la valeur précédente n'est pas forcément la valeur i-1
    previous = 0
    # On initialise une liste vide des éléments à supprimer
    toDelete = []
    # On parcours la liste à trier
    for i in range(len(toSort)):
        # Si l'élément est conforme, il devient le nouveau "modéle"
        if previous <= toSort[i]:
            previous = toSort[i]
        # Sinon, il est mis sur la liste de suppresion
        else:
            toDelete.append(i)
    
    # On inverse la liste, afin que la suppresion des éléments ne perturbe pas la place des autres éléments
    toDelete.reverse()
    # On supprime tout les éléments non-conformes
    for i in toDelete:
        del toSort[i]

# On teste la fonction
liste = [*range(100)]
shuffle(liste)
print(liste)
StalinSort(liste)
print(liste)