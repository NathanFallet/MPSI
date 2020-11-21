# On définit la fonction pseudoAleatoire
def pseudoAleatoire(n, g):
    # On reprend la fonction pseudoAleatoireSuivant de l'exercice précedent
    def pseudoAleatoireSuivant(n):
        n = int(str(n)[-10:])
        n = str(n ** 2)
        while len(n) < 20:
            n = "0" + n
        n = int(n[5:15])
        return n
    
    # On initialise une liste vide
    liste = []
    # On effectue n fois
    for i in range(n):
        # On prend la valeur aléatoire suivante
        g = pseudoAleatoireSuivant(g)
        # On l'ajoute à la liste, après l'avoir divisée par 10**10
        liste.append(g / (10**10))
    
    # On retourne la liste
    return liste

print(pseudoAleatoire(10, 1111))