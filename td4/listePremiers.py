# On importe la fonction isqrt(), donant la partie entière de la racine carrée
from math import isqrt

# Défintion d'une fonction pour avoir la liste des diviseurs
def listeDiviseurs(nombre):
    # On initialise une liste
    diviseurs = []
    # On parcours la liste tant que i <= √nombre
    for i in range(1, isqrt(nombre) + 1):
        # Si on trouve un diviseurs
        if nombre % i == 0:
            # Alors on l'ajoute à a liste, ainsi que son complément
            diviseurs.append(i)
            # On vérifie que on n'ajoute pas deux fois le même élément
            if nombre // i != i:
                diviseurs.append(nombre//i)

    # On retourne la liste des diviseurs
    return diviseurs

# On demande un nombre
n = int(input("Entrez un nombre : "))

# On initialise une liste
l = []
# On lance la boucle
for i in range(2, n):
    # Si il n'y a que 2 éléments dans la liste des diviseurs de n (donc 1 et n, logiquement)
    if len(listeDiviseurs(i)) == 2:
        # Alors cela signifie que n est premier et on l'ajoute à la liste
        l.append(i)

# On affiche la liste
print(l)