# On importe les fonctions et valeurs
from random import shuffle
from math import inf


# On définit un premier alogrithme, qui prend une par une les valeurs, dans l'ordre
def onePerOne(toSort):
    # On initialise une liste vide
    new = []
    # On effectue deux copies de la liste à trier, pour éviter de changer la liste originelle
    toSortCopy = toSort.copy()
    toSortCopy2 = toSort.copy()

    # On parcours la copie, pour éviter que les suppresions dans la liste originelle perturbe la boucle
    for i in toSortCopy2:
        # On initialise un minimum à l'infini, et l'index à 0
        low = inf
        index = 0

        # Pour chaque élément de la liste
        for j in range(len(toSortCopy)):
            # On regarde si il est plus petit que le minimum
            if low > toSortCopy[j]:
                # Si oui, il devient le nouveau minimum
                low = toSortCopy[j]
                index = j

        # On retire l'élément de la liste de base avec .pop() pour l'ajouter à la nouvelle liste
        new.append(toSortCopy.pop(index))
    # On repète cela autant de fois que pour que la liste de base soit vide
    
    # On retourne la nouvellle liste
    return new


# On définit un deuxième algorithme, qui lui échange les éléments de la liste de base jusqu'à ce qu'elle soit trié
def swapSort(toSort):
    # On définit un booléen indiquant la fin du tri
    finished = False

    # On effectue une copie de la liste, pour éviter de changer la liste originelle
    toSortCopy = toSort.copy()

    # Tant que la liste n'est pas triée
    while not finished:
        # On fait l'hypothèse que la liste est trié
        finished = True

        # On parcours la liste, à l'exception du dernier élément
        for i in range(len(toSortCopy) - 1):
            # Si une paire d'élément n'est pas rangée
            if toSortCopy[i+1] < toSortCopy[i]:
                # On utilise un double assignement pour echanger leurs places
                toSortCopy[i+1], toSortCopy[i] = toSortCopy[i], toSortCopy[i+1]

                # Et l'hypothèse que la liste était rangé est donc fausse
                finished = False
        # On continue jusqu'à ce que l'hypothèse soit vraie
    
    # On retourne la liste triée
    return toSortCopy

# On définit un troisième algorithme qui supprime tout élément non conforme au tri
# Note, ce n'est pas un vrai algorithme de tri, mais une blague plus qu'autre chose
def stalinSort(toSort):
    # On effectue une copie de la liste, pour éviter de changer la liste originelle
    toSortCopy = toSort.copy()

    # On initialise la valeur précédente à l'infini négatif, car la valeur précédente n'est pas forcément la valeur i-1
    previous = -inf
    # On initialise une liste vide des éléments à supprimer
    toDelete = []
    # On parcours la liste à trier
    for i in range(len(toSortCopy)):
        # Si l'élément est conforme, il devient le nouveau "modéle"
        if previous <= toSortCopy[i]:
            previous = toSortCopy[i]
        # Sinon, il est mis sur la liste de suppresion
        else:
            toDelete.append(i)
    
    # On inverse la liste, afin que la suppresion des éléments ne perturbe pas la place des autres éléments
    toDelete.reverse()
    # On supprime tout les éléments nou-conformes
    for i in toDelete:
        del toSortCopy[i]
    
    # On retourne la liste "triée"
    return toSortCopy


# On créer une liste avec tout les éléments de 1 à 200
listToSortCopy = list(range(1, 201))
# Et on la mélange
shuffle(listToSortCopy)

# On créer une liste avec tout les éléments de 1 à 100, deux fois
listToSortCopyRepeat = list(range(1, 101)) * 2
# Et on la mélange
shuffle(listToSortCopyRepeat)

# On lance ensuite les algorithme de tri et affiche les réponses
print(onePerOne(listToSortCopy))
print()
print(onePerOne(listToSortCopyRepeat))
print()
print(swapSort(listToSortCopy))
print()
print(swapSort(listToSortCopyRepeat))
print()
print(stalinSort(listToSortCopy))
print()
print(stalinSort(listToSortCopyRepeat))