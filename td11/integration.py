# Imports
from math import trunc

# Borne sup d'une fonction
def sup(f, a, b):
    x = a
    s = abs(f(a))
    while x <= b:
        x += 0.00001 # Pas à ajuster
        s = max(s, abs(f(b)))
    return sup

# Rectangle par la gauche
def rectangle_g(f, fp, a, b, e):
    M1 = sup(f, a, b)
    n = trunc((b-a)**2*M1/e) + 1
    A = 0
    p = (b-a)/n
    for k in range(n):
        A = A + f(a + k*p)
    return p*A

# Rectangle par la droite
def rectangle_d(f, fp, a, b, e):
    M1 = sup(f, a, b)
    n = trunc((b-a)**2*M1/e) + 1
    A = 0
    p = (b-a)/n
    for k in range(1, n-1):
        A = A + f(a + k*p)
    return p*A

# Rectangle par le milieu
def rectangle_d(f, fp, a, b, e):
    M1 = sup(f, a, b)
    n = trunc((b-a)**2*M1/e) + 1
    A = 0
    p = (b-a)/n
    for k in range(0):
        A = A + f(a + p/2 + k*p)
    return p*A
