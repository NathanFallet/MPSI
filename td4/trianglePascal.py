# On demande un nombre
n = int(input("Entrez un nombre : "))

# On initialise la liste
triangle = [[1]]
# On lance la boucle
for i in range(1, n+1):
    # On ajoute une nouvelle liste pour cet étage, avec le premier élément initialisé
    triangle.append([1])
    # On effectue pour chaque valeur à ajouter
    for j in range(i - 1):
        # On calcule grace à la formule du triangle de Pascal
        triangle[i].append(triangle[i-1][j] + triangle[i-1][j+1])
    # On rajoute le 1 de fin de ligne
    triangle[i].append(1)

# On affiche chaque ligne du triangle 1 à 1
for i in triangle:
    print(" ".join([str(j) for j in i])) # Le " ".join(...) est purement cosmétique, et pourrait être remplacée par i