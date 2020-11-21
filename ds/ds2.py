# Ce qui a été fait pendant le DS 2. Si vous avez eu le temps d'aller plus loin, n'hésitez pas à suggérer la suite

from math import log, sin, atan, pi

def phi(x):
    if x < -2:
        return -2 * log(abs(x)) + 1
    elif x <= 5:
        return 4 * sin(x)
    else:
        return atan(x) - pi

def sigma(n):
    val = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            val += i * j * j
    return val

def minmaxListe(t):
    min_val = None
    max_val = None
    for i in t:
        if not min_val:
            min_val = i
        elif i < min_val:
            min_val = i
        
        if not max_val:
            max_val = i
        elif i > max_val:
            max_val = i
    return [min_val, max_val]

def pal(mot):
    size = len(mot)

    for i in range(size):
        if mot[i].lower() != mot[size-1-i].lower():
            return False

    return True

def u(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return 3 * u(n-1) - 2 * u(n-2)

def chiffres(n):
    if n == 0:
        return [0]
    L = []
    while n != 0:
        L.append(n % 10)
        n = n // 10
    return L[::-1]

def narcisse(n):
    t = chiffres(n)
    p = len(t)

    somme = 0
    for i in t:
        somme += i ** p

    return n == somme

def nombres_narcissiques(n):
    l = []

    for i in range(n + 1):
        if narcisse(i):
            l.append(i)
    
    return l

def premier(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    if n == 0 or n == 1:
        return False

def nombres_premiers_narcissiques(n):
    l = []

    for i in range(n + 1):
        if narcisse(i) and premier(i):
            l.append(i)
    
    return l

def pseudoAleatoireSuivant(a):
    carre = a ** 2
    s = str(carre)
    while len(s) < 20:
        s = "0" + s
    return int(s[5:15])

def pseudoAleatoire(n, g):
    last = g
    l = [last / 10**10]
    for i in range(n):
        last = pseudoAleatoireSuivant(last)
        l.append(last / 10**10)
    return l
