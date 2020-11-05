""" Définition des fonctions """

# Définition de la fonction insertion
def insertion(liste, rang, élément):
    # Si on est en dehors de la liste, alors on indique qu'il y a une erreur
    if abs(rang) > len(liste):
        raise IndexError("Index out of range")

    # On retourne la liste de base avec le nouvel élément
    return liste[:rang] + [élément] + liste[rang:]


# Définition de la fonction miroir
def miroir(liste):
    # On initialise une liste vide
    sortie = []
    # On parcours la liste à l'envers, grâce à reversed()
    for i in range(len(liste)):
        # On ajoute les éléments de la liste initiale à la nouvelle liste
        sortie.append(liste[-i])
    
    # On retourne la nouvelle liste
    return sortie


# Définition de la fonction coupe
def coupe(liste, rang1, rang2):
    # On initialise un booléen
    retourné = False
    if abs(rang1) > len(liste) or abs(rang2) > len(liste):
        raise IndexError
    # On vérifie que les rangs soit dans le bon ordre
    if rang1 > rang2:
        # Sinon, on utilise un double assignement pour échanger les valeurs, et changer notre booléen
        rang1, rang2 = rang2, rang1
        retourné = True

    # On initialise une liste vide
    sortie = []
    # On parcours une partie réduite de la liste
    for i in range(rang2 - rang1):
        # Et on prend les éléments
        sortie.append(liste[i + rang1])
    
    # Si notre booléen est vrai, on retourne la liste
    if retourné:
        sortie = miroir(sortie)
    
    # On retourne la nouvelle liste
    return sortie


# Définition de la fonction comptage
def comptage(liste, élément):
    # On initialise le compteur
    sortie = 0
    # On parcours les éléments de la liste
    for i in liste:
        # Si on trouve une équivalence
        if i == élément:
            # On incrémente le compteur
            sortie += 1 # sortie = sortie + 1
    
    # On retourne le compteur
    return sortie


# Définition de la fonction suppresion
def suppresion(liste, rang):
    # Si on est en dehors de la liste, alors on indique qu'il y a une erreur
    if rang >= len(liste):
        raise IndexError("Index out of range")

    # On initialise une liste
    sortie = []
    # On parcours la liste
    for i in range(len(liste)):
        # Si on est au rang de l'objet à supprimer
        if i == rang:
            # Alors on l'ignore. continue stoppe l'itération actuelle de la boucle et passe à la suivante.
            continue
        # Sinon, on ajoute l'élément à la liste
        sortie.append(liste[i])
    
    # On retourne la nouvelle liste
    return sortie



""" Code principal """

# On demande la taille de la liste
taille = int(input("Taille de la liste : "))
# On initalise la liste
l = []
# Puis, autant de fois que la taille de la liste
for i in range(taille):
    # On demande un élément que l'on ajoute à la liste
    l.append(int(input("Entrez l'élément de rang {} : ". format(i))))


# On demande les paramètres pour l'insertion
élément = int(input("Quel élément voulez vous inserer dans la liste : "))
index = int(input("A quel position : "))
# On applique la fonction insertion
l = insertion(l, index, élément)
# On affiche le résultat
print(l)


# On applique la fonction miroir
l = miroir(l)
# On affiche le résultat
print(l)


# On demande les paramètres pour la coupe
index = int(input("Début de la coupe : "))
index2 = int(input("Fin de la coupe : "))
# On applique la fonction insertion
l = coupe(l, index, index2)
# On affiche le résultat
print(l)


# On demande le paramètre pour la recherche
élément = int(input("Quel élément voulez vous rechercher : "))
# On affiche le résultat
print(comptage(l, élément))


# On demande le paramètre pour la suppresion
index = int(input("Quel est le rang de l'élement à supprimer : "))
# On applique la fonction
l = suppresion(l, index)
# On affiche le résultat
print(l)