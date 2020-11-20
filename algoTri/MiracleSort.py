from random import shuffle

# On définit une fonction MiracleSort
# Cet algorithme attend que la liste se trie toute seule.
# Purement humoristique, c'est algorithme de tri le plus inefficace
def MiracleSort(toSort):
     # On défini une fonction auxiliaire IsSorted
    def IsSorted(inList):
        # Si la liste est trié, son minimum est le premier nombre
        minimum = inList[0]
        # On teste pour chaque élément de la liste
        for i in inList[1:]:
            # Si il est inférieur au minimum, alors la liste n'est pas triée
            if i < minimum:
                # Donc on sort de la fonction
                return False
        
            # Le nombre que l'on vient de tester est donc le nouveau minimum
            minimum = i
        
        # Si il n'y a aucun problème, la liste est donc triée
        return True
    
    # On définie une fonction auxilliaire waitForMiracle
    def waitForMiracle():
        pass # Instruction vide ne faisant rien
    
    # Tant que la liste n'est pas triée
    while not IsSorted(toSort):
        # On attends un miracle
        waitForMiracle()
    
    # On retourne la liste
    return toSort

# On teste la fonction
liste = [*range(10)]
shuffle(liste)
print(liste)
print(MiracleSort(liste))