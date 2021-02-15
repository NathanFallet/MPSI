from typing import Tuple

def divEuclid(a: int, b: int) -> Tuple[int, int]:
    q, r = 0, a
    while r > b:
        q += 1
        r -= b
    return q, r

""" 1)
Étape 0 : q = 0, r = 17, r > b = True
Étape 2 : q = 1, r = 12, r > b = True
Étape 3 : q = 2, r = 7, r > b = True
Étape 4 : q = 3, r = 2, r > b = False
"""

""" 2)
b est strictement positif
Donc, vu que la boucle contient r -= b, r est décroissant
La boucle n'effectue aucune opération sur b, il est constant
Donc éventuellement, r > b deviendra faux
"""