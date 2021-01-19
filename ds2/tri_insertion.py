def tri_insertion(l: list) -> list:
    if len(l) == 1: # Si la liste ne contient qu'un seul élément
        return l # On retourne la même liste
    
    tête, queue = l[0], l[1:] # On sépare en la tête (élément 0) et la queue (le reste)
    queue = tri_insertion(queue) # On tri la queue

    for i in range(len(queue)): # On teste pour chaque élément de la queue
        if tête < queue[i]: # Si la tête et plus petit que l'élément
            return queue[:i] + [tête] + queue[i:] # Alors on le place juste avant
    
    return queue + [tête] # Sinon, la tête est le plus grand élément, à la fin