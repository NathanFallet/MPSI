"""
En Python, les variables n'ont pas de type particulier, ainsi on peut faire :

>>> var = 3
>>> print(var) -> 3
>>> var = "abc"
>>> print(var) -> abc

Mais cela peut poser des problèmes car on peut passer un type de variable différent à une fonction sans le faire exprès et avoir des résultats surprenants.
"""

def double(x):
    return x * 2

"""
>>> double(3) -> 6
>>> double("abc") -> abcabc

La fonction double n'a clairement pas été faite pour faire des opérations avec les booléens.


Mais heuresement, Python supporte les annotations de types, permettant d'indiquer à votre IDE (environement de travail) quels types sont neccessaires pour quelles fonctions.
Cela ne changera rien à l'éxécution du code, mais ça aide à mieux debbuger son programme.
"""

def double_int(x: int) -> int: # On indique que x doit être un int, et que la fonction retourne un int
    return x * 2

"""
>>> double_int(3) -> 6
>>> double_int("abc") -> abcabc, Mais l'IDE signalera un avertissement :
 - Argument of type "Literal['abc']" cannot be assigned to parameter "x" of type "int" in function "double_int"
 - "Literal['abc']" is incompatible with "int"

L'IDE nous dit que l'argument passé, "abc", ne doit pas être assigné à x, car il est de type int.
Car le type de "abc", str, est incompatible avec le type de int.


Mais, prenons cette fonction :
"""

def print_twice(chaine: str) -> None: # Prend chaine, qui doit être un str, et ne retourne rien
    print(chaine, chaine)

"""
>>> print_twice("a") -> "a a"
>>> print_twice(3) -> "3 3", mais l'IDE affiche un avertissement

Pourtant print(int) marche de la même manière et donne le même résultat que print(str).
Alors comment indiquer la possibilité d'avoir plusieurs types possible pour un paramètre ?
Avec l'aide de l'Union :
"""

from typing import Union

def print_twice_2(chaine: Union[str, int]) -> None:
    print(chaine, chaine)

"""
Maitenant, l'IDE n'affichera pas d'avertissement si vous passer un int en paramètre de la fonction.


Autres exemples :
"""

# Annotation de type et paramètre par défaut
def puissance_de_deux(x: int = 3) -> int: # x doit être un int et vaut 3 par défaut, la fonction retourne un int
    return 2 ** x


from typing import Tuple

# Annotation représentant un tuple
def div_euclid(x: int, y: int) -> Tuple[int, int]: # Prend x et y, des ints et retourne un tuple de la forme (int, int)
    return x // y, x % y


# Tuple de taille inderterminée
def tuple_range(start: int, end: int) -> Tuple[int, ...]: # Prend start et end, et retourne un tuple de int, de taille variante
    return tuple(range(start, end)) # Renvoie un tuple avec toutes les valeurs entre start et end, start inclus


from typing import List

# Type de listes
def double_int_list(l: List[int]) -> List[int]: # Prend l une liste de ints, et retourne une liste de ints
    return list(map(double_int, l))


from typing import Any

# Listes de tout type
def double_list(l: List[Any]) -> List[Any]:# Prend une liste quelconque et retourne une liste quelconque
    out = []
    for i in l:
        out += [i, i]
    return out # Double tout les éléments d'une liste