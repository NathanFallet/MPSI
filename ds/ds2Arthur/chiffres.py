# On définit une fonction chiffres
def chiffres(n):
    # On gère le cas où n = 0, en retournant [0]
    if n == 0:
        return [0]
    
    # Sinon, on initialise une liste vide
    L = []
    # Et tant qu'il nous reste des chiffres
    while n != 0:
        # On ajoute à la liste le dernier chiffre
        L.append(n % 10)
        # On enlève se dernier chiffre en divisant par 10
        n = n // 10
    
    # On retourne la liste, inversé des chiffres
    return [*reversed(L)]
