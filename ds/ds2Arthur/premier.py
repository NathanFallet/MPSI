# On importe la fonction isqrt
from math import isqrt

# On définit une fonction premier
def premier(n):
    # On définit une fonction pour obtenir la liste des diviseurs
    def diviseurs(n):
        # On initialise une liste
        diviseurs = []
        # On parcours la liste tant que i <= √n
        for i in range(1, isqrt(n) + 1):
            # Si on trouve un diviseur
            if n % i == 0:
                # Alors on l'ajoute à a liste, ainsi que son complément
                diviseurs.append(i)
                # On vérifie que on n'ajoute pas deux fois le même élément
                if n // i != i:
                    diviseurs.append(n//i)

        # On retourne la liste des diviseurs
        return diviseurs
    
    # Si le nombre n'a que deux diviseurs, alors il est premier et on retourne vrai, sinon on retourne faux
    if len(diviseurs(n)) == 2:
        return True
    return False