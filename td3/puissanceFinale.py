# On demande deux nombres
a, n = int(input("Entrez a : ")), int(input("Entrez n : "))

# On définit une fonction encadrement
def encadrement(nombre):
    # On initialise la valeur de l'encadrement
    encadrement = 0
    # Tant que l'encadrement est trop petit, on l'augmente
    while nombre / (10 ** encadrement) >= 1:
        encadrement += 1
    
    return encadrement

# On initialise la liste des puissances
puissancesFinales = []
# On parcours la liste des nombres plus petits que n
for i in range(1, n):
    # On obtient l'encadrement du nombre
    taille = encadrement(i)
    # On obtient les nombres de fin, suivant l'encadrement de i
    finNombre = (a ** i) % (10 ** taille)

    # Si la fin et la puissance coincide, on a une puissance finale
    if finNombre == i:
        # On l'ajoute donc à la liste
        puissancesFinales.append(str(i))

# On affiche ensuite la liste des puissances finales
print("Les puissances finales de {} plus petites ou égales à {} sont : {}".format(a, n, " ".join(puissancesFinales)))