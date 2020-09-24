# On demande le nombre
a = input("Donnez un nombre : ")

# On cree une liste vide
d = []

# On parcours tous les nombres jusqu'a a
for b in range(1, a + 1):
    # On regarde si il est divisible par b
    if a % b == 0:
        # On l'ajoute a la liste
        d.append(b)

# On affiche la liste
print(d)