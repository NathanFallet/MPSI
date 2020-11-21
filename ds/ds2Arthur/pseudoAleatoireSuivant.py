# On définit la fonction pseudoAleatoireSuivant
def pseudoAleatoireSuivant(n):
    # On prend uniquement les 10 derniers chiffres de n
    n = int(str(n)[-10:])
    # On le met au carré
    n = str(n ** 2)
    # On rajoute les 0 à gauche
    while len(n) < 20:
        n = "0" + n
    # On prend les chiffres de 6 à 15
    n = int(n[5:15])

    # On retourne le nouveau nombre n
    return n