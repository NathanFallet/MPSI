# On définit une fonction nombres_narcissiques
def nombres_narcissiques(n):
    # On reprend la fonction narcisse de l'exercice précedent
    def narcisse(n):
        def chiffres(n):
            if n == 0:
                return [0]
            L = []
            while n != 0:
                L.append(n % 10)
                n = n // 10
            return [*reversed(L)]
        chiffre = chiffres(n)
        somme = 0
        for i in chiffre:
            somme += i**len(chiffre)
        if somme == n:
            return True
        return False
    
    # On initialise une liste vide
    liste = []
    # Pour chaque nombre jusqu'à n
    for i in range(n):
        # Si le nombre est narcissique
        if narcisse(i):
            # On l'ajoute à la liste
            liste.append(i)
    
    # On retourne la liste
    return liste