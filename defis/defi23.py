"""

Nous dirons qu'un nomber entier positif n est parent du nombre a deux chiffres ab
si son chiffre des unites est b et si ses autres chiffres sont differents de 0 et
que leur somme est a.

Par exemple, les parents de 31 sont 31, 121, 211 et 1111.

Combien de nombres a deux chiffres sont diviseurs de tous leurs parents ?

"""

# Fonction pour obtenir les unites
def unit(number):
    return number % 10

# Fonction pour obtenur les dizaines
def ten(number):
    return unit(number // 10)

# Fonction qui check si n est parent de ab
def check(n, ab):
    # On verifie si b est l'unite de n
    if unit(n) != unit(ab):
        return False

    # On verifie que les autres chiffres sont differents de zero
    if ten(n) == 0:
        return False
    
    # On fait la somme des chiffres sans les unites
    sum = 0
    withoutUnit = n - unit(ab)
    for i in str(withoutUnit):
        sum += int(i)

    # On verifie si la somme est bien a
    if sum != ten(ab):
        return False

    # Tout est ok
    return True

# Fonction qui check si un nombre est diviseur d'un autre
def isDivisor(a, b):
    return b % a == 0

# Phase de test
print(check(31, 31), check(121, 31), check(211, 31), check(1111, 31))


