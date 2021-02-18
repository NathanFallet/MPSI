""" Exemples lambdas """

# On crée un lambda générant un lambda de polynôme de degré 2
secondDegré = lambda a, b, c: lambda x: a*(x**2) + b*x + c

fonction1 = secondDegré(2, 3, -4) # Ici, le polynôme est 2x² + 3x - 4
fonction2 = secondDegré(-0.5, 0, 3) # Ici, le polynôme est -0.5x² + 3


""" Exemples générateurs """

from typing import Callable, Generator
from math import isqrt, sqrt, log

# On créer un générateur range ou l'argument step est une fonction
def funcRange(start: float, stop: float, funcStep: Callable[[float], float]) -> Generator[float, None, None]:
    a = start
    while a < stop:
        yield a
        a = funcStep(a)

# On définit un range ou la valeur double à chaque fois
# On prend toute les puissances de 2 entre 1 inclu et 1000 exclu
# On utilise un lambda à la place d'un fonction car on n'en aura sûrement pas besoin ailleurs
puissanceDeDeux = funcRange(1, 1000, lambda a: a*2)

print("Puissance de deux")
for i in puissanceDeDeux:
    print(i)
print()


# On définit un générateur retournant les nombres de fibbonacci
def fibbonacci(total: int) -> Generator[int, None, None]:
    # On prend a=0, et b=1
    a, b, c = 0, 1, 0
    while c < total:
        # On donne a
        yield a
        # On prend a=b et b=a+b
        a, b = b, a + b
        c += 1

print("Fibbonacci")
for i in fibbonacci(10):
    print(i)
print()

# On définit un générateur range qui s'arrête dés qu'une condition devient fausse
def condRange(start: float, stopCond: Callable[[float], bool], step: float) -> Generator[float, None, None]:
    a = start
    while stopCond(a):
        yield a
        a += step

# On définit un range qui commence à 1 et s'arrête dès que la somme des entiers de 1 à n dépasse 100
totalSumLowerHundred = condRange(0, lambda a: (a*(a+1))//2 < 100, 1)

print("Somme inférieure à 100")
for i in totalSumLowerHundred:
    print(i)
print()

# On définit un générateur nous donnant des trinômes de Pythagore (méthode naive)
def triPythagore(total: int):
    a, b, c = 3, 4, 0
    while c < total:
        if isqrt(a**2 + b**2) == sqrt(a**2 + b**2):
            yield a, b
            c += 1
        b += 1
        if log(b) > log(a) * 3:
            a += 1
            b = a

print("Trinôme de Pythagore")
for i, j in triPythagore(10):
    print(i, j)
print()