from random import shuffle
from typing import Any, List
from time import perf_counter

# On définit une fonction BubbleSort
# Cet algorithme marche en comparant les éléments voisins deux à deux et en échangeant leurs places si besoin
# Cet type de tri possède une bonne efficacité et est constant. Il trie aussi bien petite et grandes listes
# Il fait un tri sur place, ainsi il ne renvoi rien, et ne fait que modifier la liste originelle
def BubbleSort(toSort: List[Any]) -> None:
    # On effectue une copie de la liste, pour éviter de changer la liste originelle

    # On répéte autant de fois qu'il y a d'éléments dans la liste
    for i in range(len(toSort)):
        # On fait l'hypothèse que la liste est triée
        finished = True

        # On parcours la liste, à l'exception du premier élément, car on compare des paires, et des i derniers, car on est garanti qu'ils sont rangés
        for j in range(1, len(toSort) - i):
            # Si une paire d'élément n'est pas rangée
            if toSort[j] < toSort[j-1]:
                # On utilise un double assignement pour echanger leurs places
                toSort[j], toSort[j-1] = toSort[j-1], toSort[j]
                # L'hypothèse était donc fausse
                finished = False

        # Mais si l'hypothèse était vraie, on retourne la liste maintenant    
        if finished:
            return

# On teste la fonction
liste = [*range(100)]
shuffle(liste)
#print(liste)
t0 = perf_counter()
BubbleSort(liste)
t1 = perf_counter()
print(t1 - t0)
#print(liste)