"""
Les générateurs sont des fonctions très spéciale en Python :
Elle ne calcule pas toutes leurs sorties directement.
À la place, elle calcule une première valeur, la renvoie, et se met en pause jusqu'à temps que l'on ai besoin de la prochaine valeur.

La fonction générateur la plus répendue et la fonction range(x, y) :
Elle ne créer pas une liste avec les nombres de x à y, mais elle calcule x, puis dès que l'on a besoin, calcule x+1 ...
Tout cela tant que x+n != y.

La fonction range peut être facilement redéfinie (ici, on ne prendra que les cas où x < y) :
"""

from typing import Generator

def newRange(start: int, stop: int) -> Generator[int, None, None]:
    a = start
    while a != stop:
        yield a
        a += 1

# On peut se servir de notre nouveau range comme de l'ancien range

print("On affiche les nombres de 8 à 13")
for i in newRange(8, 14):
    print(i) # Affiche les nombres de 8 à 13
print()

"""
Petite explication de la syntaxe :

Même si la définition resemble à une fonction, il y a des differences radicales.
En effet, on n'utilise pas return mais yield :
Ainsi yield vas retourner une valeur et même la fonction en pause, ainsi les variables garderont leurs valeurs.

Un gros avantage des générateurs et de pouvoir faire des boucles infinies sans causer de problèmes pour le programme
"""

def alternatingInt(value: int) -> Generator[int, None, None]:
    a = value
    while True:
        yield a
        a *= -1

# On ne peut pas s'en servir comme un range, car sinon on causerait une boucle infinie.
# Mais on peut obtenir la valeur suivante via next(generator)
# Vu que le générateur est infini, il ne sera jamais à court de valeurs

print("On multiple les nombres de 1 à 5 par 5 ou -5")
alternator = alternatingInt(-5)
for i in range(1, 6):
    print(i * next(alternator))
print()

"""
On peut même faire des générateurs retournant autre chose que des nombres
"""

def alphabet(end: str) -> Generator[str, None, None]:
    a = ord("A")
    while a <= ord(end):
        yield chr(a)
        a += 1

print("On affiche l'alphabet (jusque J)")
for i in alphabet("J"):
    print(i)
print()

"""
Si besoin, on peut transformer les résultats d'un générateur en liste via l'unpacking :
"""

alphabeta = [*alphabet("Z")] # On utilise la syntaxe [*generateur] pour obtenir une liste de tout les éléments générés par le générateur

print("On affiche l'alphabet, sur une ligne")
print(" ".join(alphabeta))