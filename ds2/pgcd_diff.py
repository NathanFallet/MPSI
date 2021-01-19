from typing import Any

def plus_grand(a: Any, b: Any) -> Any:
    return a if b < a else b # Utilisation du if sur une seule ligne


def plus_petit(a: Any, b: Any) -> Any:
    return a if a < b else b # Utilisation du if sur une seule ligne


def pgcd_diff(a: int, b: int) -> int:
    diff = abs(a - b) # La fonction absolu nous assure d'avoir la différence positive
    if diff == 0: # Si la différence est nulle, soit a = b, on retourne a
        return a
    # Sinon, on tente pour le min entre a et b et la différence
    return pgcd_diff(plus_petit(a, b), diff)


"""
Alternativement, les fonctions max et min font l'affaire :

max(1, 2) # Retourne 2

min(8, 1, 7, 3) # Retourne 1
"""