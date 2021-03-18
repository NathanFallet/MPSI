"""
Algo de résolution approchée d'une équation
"""

# Balayage
def balayage(a, N, f):
    x = a
    while f(a) * f(x) > 0:
        x = x + 10**(-N)
    return x

# Dichotomie
def dichotomie(f, a, b, ε):
    while b-a > ε:
        m = (b-a)/2
        if f(a)*f(m) < 0:
            b = m
        elif f(a)*f(m) > 0:
            a = m
        else:
            a, b = m, m
    return (a, b)

# Ça marche pas, à inspecter (boucle infinie)
#print("Dichotomie :\nx^2 - 2 = 0 ssi x ≈", dichotomie(f, 1, 2, 0.0001))

# Secante
def secante(a, b, f, ε):
    x0 = a
    x1 = b
    while x1 - x0 > ε:
        t = (f(b) - f(x0)) / (b - x0)
        p = f(b) - t * b
        x1 = x0
        x0 = (-p)/t
    return x1

# 1.
def g(x):
    return x**2 - 10

print("x^2 = 10\t ssi x =", balayage(3, 4, g))

# 2.
def h(x):
    return x**3 - 3*x + 1

print("x^3 + 1 = 3x\t ssi x =", balayage(-2, 4, h))

# 3.
def f(x):
    return x**2 - 2

print("x^2 - 2 = 0\t ssi x =", balayage(1, 4, f))

# 4.
from math import cos, sin

print("cos(x) = 0\t ssi x =", balayage(1, 4, cos))

# 5.
def cs(x):
    return cos(x) - sin(x)

print("cos(x) = sin(x)\t ssi x =", balayage(0, 4, cs))
