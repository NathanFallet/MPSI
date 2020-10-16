# On définit une fonction de moyenne pondéré
def moyenne(notes, coefs):
    # On vérifie que les listes soient de même taille, sinon, on indique l'erreur
    if len(notes) != len(coefs):
        raise IndexError("Lists lengths do not match")

    # On initialise deux variables
    total = 0
    totalCoefs = 0
    # On parcours les deux listes en même temps, car elles sont de même taille
    for i in range(len(notes)):
        # On fait la somme pondéré des notes, et la somme des coefs
        total += notes[i] * coefs[i]
        totalCoefs += coefs[i]
    
    # On retourne la moyenne pondérée
    return total/totalCoefs


# On demande la taille de la liste de notes
taille = int(input("Taille de la liste de notes : "))
# On initalise la liste
n = []
# Puis, autant de fois que la taille de la liste
for i in range(taille):
    # On demande un élément que l'on ajoute à la liste
    n.append(int(input("Entrez l'élément de rang {} : ". format(i))))

# On passe une ligne
print()

# On demande la taille de la liste de coefs
taille = int(input("Taille de la liste de coefs : "))
# On initalise la liste
c = []
# Puis, autant de fois que la taille de la liste
for i in range(taille):
    # On demande un élément que l'on ajoute à la liste
    c.append(int(input("Entrez l'élément de rang {} : ". format(i))))

# On passe une ligne
print()

# On affiche le résultat
print(moyenne(n, c))