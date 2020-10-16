# On définit la fonction d'encryption
def crypte(chaine, clef):
    sortie = ""
    for i in chaine:
        # On regarde si on a une minuscule
        if (ord(i) >= 97) and (ord(i) <= 122):
            # On ajoute la clef, et utilise le modulo pour obtenir la nouvelle lettre
            sortie += chr(((ord(i) + clef - 97) % 26) + 97)
        # On regarde si on a une majuscule
        elif (ord(i) >= 65) and (ord(i) <= 90):
            # On ajoute la clef, et utilise le modulo pour obtenir la nouvelle lettre
            sortie += chr(((ord(i) + clef - 65) % 26) + 65)
        # Sinon, on ne fait rien
        else:
            sortie += i
    
    # On retourne la nouvelle chaine
    return sortie

# La decryption est juste l'encryption à l'envers
def decrypte(chaine, clef):
    # On donne juste l'encryption avec l'opposé de la clef
    return crypte(chaine, -clef)

# On demande une chaine de charactères
c = input("Entrez un chaine de charactères : ")
# On demande la clef
n = int(input("Quelle est la clef : "))

# On affiche le résultat
print(crypte(c, n))
print(decrypte(c, n))