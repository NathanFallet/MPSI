# On importe la fonction floor
from math import floor

# On définit un fonction tirageDe
def tiragesDe(n, g):
    # On reprend la fonction pseudoAleatoire de l'exercice précedent
    def pseudoAleatoire(n, g):
        def pseudoAleatoireSuivant(n):
            n = int(str(n)[-10:])
            n = str(n ** 2)
            while len(n) < 20:
                n = "0" + n
            n = int(n[5:15])
            return n
        liste = []
        for i in range(n):
            g = pseudoAleatoireSuivant(g)
            liste.append(g / (10**10))
        return liste
    
    # On initialise une liste vide
    liste = []
    # On tire n valeurs aléatoire
    tirage = pseudoAleatoire(n, g)
    # Pour chaque valeur tirée
    for i in tirage:
        # On la multiplie par 6, prend la partie entière et ajoute 1, puis on l'ajoute à la liste
        liste.append(floor(i * 6) + 1)
    
    # On retourne la liste
    return liste