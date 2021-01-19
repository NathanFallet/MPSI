from typing import Tuple

def divEuclide(a: int, b: int) -> Tuple[int, int]:
    return a // b, a % b # Elle renvoie deux éléments, dans un tuple (q, r)

def pgcd(a: int, b: int) -> int:
    a, b = max(a, b), min(a, b) # Ici, a devient le max de a b, et b le min. Donc a > b
    _, r = divEuclide(a, b) # On associe les deux éléments de divEuclide à deux variables
    # Note : la variable _ est une notation pour indiquer une variable non-utilisée, ici on n'utilise pas le quotient
    if r == 0: # On regarde si le reste vaut 0
        return b # Si oui, on renvoi le résultat
    return pgcd(b, r) # Si non, on recommence avec a = b et b = r