from math import isqrt
from typing import Optional, Tuple

def bezout_iter(a: int, b: int) -> Tuple[int, int, int]:
    r2, x2, y2 = a, 1, 0 # Initialisation du rang 0
    r, x, y = b, 0, 1 # Initialisation du rang 1

    while r2 - (r2 // r) * r != 0: # Tant que r_n ne vaut pas 0
        r2, x2, y2, r, x, y = r, x, y, r2-(r2//r)*r, x2-(r2//r)*x, y2-(r2//r)*y # Le rang n-2 prend les valeurs du rang n-1, et on calcule de nouvelles valeurs pour le rang n-1

    return r, x, y # On retourne le rang n-1

def bezout_rec(a: int, b: int) -> Tuple[int, int, int]:
    # On définit une fonction auxiliaire
    def aux(c: int, d: int, n: int) -> Tuple[int, int, int]:
        if n == 0: return a, 1, 0 # Gestion du cas n = 0
        if n == 1: return b, 0, 1 # Gestion du cas n = 1

        r2, x2, y2 = aux(a, b, n-2) # Calcul du rang n-2
        r, x, y = aux(a, b, n-1) # Calcul du rang n-1

        if r2 - (r2 // r) * r == 0: # Si r_n vaut 0
            return r, x, y # On s'arrête là

        return r2-(r2//r)*r, x2-(r2//r)*x, y2-(r2//r)*y # On retourne le rang n
    
    return aux(a, b, isqrt(max(a, b))) # On appelle la fonction auxilliaire, avec n = √max(a, b)