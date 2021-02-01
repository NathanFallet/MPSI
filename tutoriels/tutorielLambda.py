"""
Les fonctions en Python ont comme utilité principale d'éviter de répéter le même code plusieurs fois.
Mais elles ont une syntaxe relativement lourde, s'étalant sur un minimum de deux lignes (contrairements aux if et for qui ont une syntaxe sur une ligne).

Et parfois, on se retrouve avec des fonctions très basique, mais qui prennent deux lignes.
Et même avec plusieurs fonctions très similaires.
Exemple : 
"""

def double(a: int) -> int:
    return a * 2

def triple(a: int) -> int:
    return a * 3

print("On affiche le double et le triple de 2 (fonctions)")
print(double(2)) # Affiche 4
print(triple(2)) # Affiche 6
print()

"""
Heuresement, il existe un moyen de régler ces deux problèmes: les fonctions lambdas anonymes.

Leur syntaxe est plus compacte et tient sur une seule ligne, pour une syntaxe plus claire :
"""

doubleLambda = lambda a: a * 2

tripleLambda = lambda a: a * 3

print("On affiche le double et le triple de 2 (lambdas)")
print(doubleLambda(2)) # Affiche 4
print(tripleLambda(2)) # Affiche 6
print()

"""
Petite explication de la syntaxe :
Le lambda en lui même est seulement "lambda var: code".

La partie var peut contenir plusieurs noms de variables, comme pour une fonction normale:
>>> lambda list: ... -> 
>>> lambda a, b, c: ...

La partie code contient (en gros) le return d'une fonction normale.
>>> lambda n: int(n) == n -> Check si n est un int

Mais le gros changement est le fait qu'il faut assigner le lambda à une variable, il n'a pas son propre nom (d'où anonyme) :
"""

# On définit un lambda qui met un nombre au carré, et l'associe à la variable a
a = lambda e: e ** 2
print("On affiche le carré de 9")
print(a(9)) # Affiche 81

# Puis on l'assigne aussi à la variable b
b = a
print(b(9)) # Affiche 81
print()

"""
Le plus gros avantage des lambdas est qu'ils peuvent être créer et retourné par des fonctions.

On peut ansi relativement facilement créer une fonction créatrice (ou même un lambda créateur) de lambdas :
"""

# On peut le faire sous la forme d'une fonction qui retourne un lambda
def lambdaFactory(a: int):
    return lambda b: a * b

# Ou à l'aide d'un lambda, qui retourne lui même un lambda
lambdaFactory2 = lambda a: (lambda b: a * b)

# On définit des lambdas à partir de notre lambdas créateur
doubleAgain = lambdaFactory(2)
tripleAgain = lambdaFactory2(3)

# Et ces lambdas marchent tout aussi bien que des fonctions normales
print("On affiche le double et le triple de 2 (lambdas de lambdas)")
print(doubleAgain(2)) # Affiche 4
print(tripleAgain(2)) # Affiche 6