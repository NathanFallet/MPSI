"""
Au tout début, on faisait de la programmation d'ordre 0, tout objet intéragissait avec les autres au même niveau.
Puis on est monté d'un ordre avec les fonctions, ainsi certains objets (les fonctions) intéragissent avec les autres objets depuis un autre niveau.

Si nous voulions encore monter d'un ordre, on aurait des fonction prennant en paramétre des fonctions.
Ainsi ces super-fonctions serait encore un niveau au dessus des fonctions habituelles.
Ceci peut potentiellement continuer à l'infini, mais l'utilité devient questionable.

On va directement commencer par un exemple que l'on va décortiquer
"""
from typing import Any, Callable, List

# Cette fonction affiche deux fois chaque élément qu'on lui donne
def printTwice(a: str) -> None:
    print(a, a)

# Cette fonction enlève le dernier élément de la liste,
# Et le donne en argument à la fonction func,
# Jusqu'à ce que la liste soit vide
def popAndFunc(l: List[str], func: Callable[[str], None]) -> None:
    while l != []:
        func(l.pop())

print("Test 1")
# On définit une liste
l = ["Jean", "Charles", "Sacha", "Marie", "François", "Michel", "Émilien", "Cristophe", "Donald"]
# On demande ainsi d'enlever le dernier élément de la liste, et de l'afficher deux fois, pour tout les éléments
popAndFunc(l, printTwice)
print()

"""
Ainsi, dans popAndFunc, la fonction func peut être n'importe quelle fonction qui prend un string en entrée et ne retourne rien
On pourrait donc lui passer print par exemple
"""

print("Test 2")
l = ["Jean", "Charles", "Sacha", "Marie", "François", "Michel", "Émilien", "Cristophe", "Donald"]
popAndFunc(l, print)
print()

"""
On peut en définir des beaucoup plus complexes
"""

def mixTwoStrings(a: str, b: str) -> str:
    a, b = a[0:len(a)//2], b[len(b)//2:]
    return a + b

printIfEndsWith = lambda end: lambda a: print(a) if a[-1] in end else None
printIfEndsWithVoyel = printIfEndsWith(("a", "e", "i", "o", "u", "y"))

def actOnNeighbouringPairs(l: List[Any], func: Callable[[Any, Any], Any], out: Callable[[Any], None]) -> None:
    for n in range(len(l)-1):
        out(func(l[n], l[n+1]))

print("Test 3")
l = ["Jean", "Charles", "Sacha", "Marie", "François", "Michel", "Émilien", "Cristophe", "Donald"]
actOnNeighbouringPairs(l, mixTwoStrings, printTwice)
print()
print("Test 4")
actOnNeighbouringPairs(l, mixTwoStrings, print)
print()
print("Test 5")
actOnNeighbouringPairs(l, mixTwoStrings, printIfEndsWithVoyel)
print()

"""
On peut même utiliser une fonction une fonction de sortie complétement différente :
"""

liste = []
print("Test 6")
actOnNeighbouringPairs(l, mixTwoStrings, liste.append)
print(liste)

"""
Pour conclure, les fonctions de haut ordre marche de la même manière que les fonctions normales.
Elle prennent juste (au moins) une autre fonction en argument.
Elle permettent, quand bien utilisée, d'éviter d'écrire du code répétitif.
"""