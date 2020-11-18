# On importe une fonction nous donnant la partie entière d'une racine
from math import isqrt

# On demande n et prépare une liste vide
n = int(input("Entrez n : "))
nombrePremiers = []

# Pour chaque nombre entre 2 et √n + 1
for i in range(2, isqrt(n) + 1):
    # On ajoute un set (liste non organisée) à la liste des nombres premiers
    nombrePremiers.append(set({}))

    # Pour chaque nombre de 2 à n
    for j in range(2, n+1):
        # Si le nombre est égal à ce que l'on teste, ou non divisible
        if j % i != 0 or j == i:
            # On l'ajoute au set (on fait l'union entre le set principal et un set contenant uniquement ce nombre)
            nombrePremiers[i-2] = nombrePremiers[i-2] | {j}

# On a maintenant une liste contenant plusieurs sets correspondant chacun aux nombres premiers à i

# Maintenant, on utilise une boucle pour faire l'intersection de tout ces sets
for i in range(1, len(nombrePremiers)):
    # On redéfinit donc le premier set comme l'intersection entre lui même et le set suivant
    nombrePremiers[0] = nombrePremiers[0] & nombrePremiers[i]

# On fini par afficher le premier set (trié), contenant l'intersection de tout les sets
print(sorted(nombrePremiers[0]))