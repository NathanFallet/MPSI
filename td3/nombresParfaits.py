# On importe les fonctions
from math import isqrt

# On demande un nombre x
x = int(input("Entrez un nombre : "))

# On met en marche la boucle
for n in  range(6, x):
    # On prépare la liste des diviseurs
    diviseurs = [1]
    # On obtient le restant de la liste
    for i in range(2, 1 + isqrt(n - 1)):
        if n % i == 0:
            diviseurs.append(i)
            diviseurs.append(n//i)

    # On vérifie que le nombre soit parfait en faisant la somme des des diviseurs
    totalSum = 0
    for i in diviseurs:
        totalSum += i

    # On affiche le résultat
    if totalSum == n:
        print("{} est parfait".format(n))