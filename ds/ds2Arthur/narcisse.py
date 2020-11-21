# On définit une fonction narcisse
def narcisse(n):
    # On reprend la fonction chiffre de l'exercice précedent
    def chiffres(n):
        if n == 0:
            return [0]
        L = []
        while n != 0:
            L.append(n % 10)
            n = n // 10
        return [*reversed(L)]
    
    # On prend la liste des chiffres de n
    chiffre = chiffres(n)
    # On initialise à 0 une variable somme
    somme = 0
    # Pour chaque chiffre de n
    for i in chiffre:
        # On ajoute à somme sa puissance p-ième
        somme += i**len(chiffre)
    
    # Si la somme est égale à n, on retourne vrai, sinon on retourne faux
    if somme == n:
        return True
    return False