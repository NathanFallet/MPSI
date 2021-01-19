from typing import List

def chiffres(a: int) -> List[str]:
    # Transforme a en string, met le tout dans une liste, et retourne
    return [i for i in str(a)]

def exo4(n: int) -> None:
    # On trie les nombres, et les joins en un str, qui devient ensuite un int
    # On fait de même en inversant la liste avant
    C, D = int("".join(sorted(chiffres(n)))), int("".join(reversed(sorted(chiffres(n)))))
    print("C = {}  D = {}  D - C = {}".format(C, D, D-C)) # On affiche les résultat
    # Si le nouveau nombre trié est quivalent à notre nombre trié actuel
    if int("".join(sorted(chiffres(D - C)))) == C:
        return # On s'arrête
    return exo4(D-C) # Sinon, on continue avec l'itération suivante