# On définit la fonction pour trouver le minimum d'une liste
def minimumListe(liste):
    # On initialise le minimum et l'index à la première valeur de la liste
    minimum = liste[0]
    index = 0
    # On parcours la liste à partir du deuxième élément
    for i in range(1, len(liste)):
        # Si on a un nouveau minimum
        if liste[i] <= minimum:
            # On remplace l'ancien minimum par le nouveau
            minimum = liste[i]
            index = i
    
    # On retourne un tuple avec les deux valeurs recherchées
    return (minimum, index)


# On définit la fonction pour trouver les minimum d'une liste
def minimumsListe(liste):
    # On utilise la fonction précédente pour obtenir le minimum de la liste
    minimum = minimumListe(liste)[0]
    # On initalise une liste vide
    index = []
    # On parcours la liste
    for i in range(len(liste)):
        # Si on trouve un élément identique au minimum
        if liste[i] == minimum:
            # On l'ajoute à la liste
            index.append(i)

    # On retourne la liste de des occurences du minimum
    return index


# On demande la taille de la liste
taille = int(input("Taille de la liste : "))
# On initalise la liste
l = []
# Puis, autant de fois que la taille de la liste
for i in range(taille):
    # On demande un élément que l'on ajoute à la liste
    l.append(int(input("Entrez l'élément de rang {} : ". format(i))))

# On passe une ligne
print()

# On affiche le résultat
print(minimumListe(l))
print(minimumsListe(l))