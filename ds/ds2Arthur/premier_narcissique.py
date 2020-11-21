# On importe la fonction isqrt
from math import isqrt

# On définit la fonction nombres_premiers_narcissiques
def nombres_premiers_narcissiques(n):
    # On reprend la fonction premier de l'exercice précedent
    def premier(n):
        def diviseurs(n):
            diviseurs = []
            for i in range(1, isqrt(n) + 1):
                if n % i == 0:
                    diviseurs.append(i)
                    if n // i != i:
                        diviseurs.append(n//i)
            return diviseurs
        if len(diviseurs(n)) == 2:
            return True
        return False
    
    # On reprend la fonction narcisse de l'exercice précédent
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
        # Si le nombre est narcissique et premier
        if narcisse(i) and premier(i):
            # On l'ajoute à la liste
            liste.append(i)
    
    # On retourne la liste
    return liste