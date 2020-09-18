# Fonction pour convertir to decimal au binaire
def dectobin(dec):
    # On défini nos variables utiles
    string = ""
    value = dec

    # Tant qu'il reste un truc
    while (value > 0):
        # On ajoute le reste à la chaine de caractères
        string = str(value % 2) + string

        # On divise par deux
        value = value >> 1

    # On retourne la chaine convertie
    return string if string else "0"

# On demande un nombre
a = int(input("Entrez un nombre : "))

# On affiche la conversion
print("Ça fait " + str(dectobin(a)) + " en binaire")
