# Question 1

# La fonction qui donne le chiffre des unites
def unite(n):
    # Le chiffre des unites correspond au reste de la division par 10
    return n % 10

# On test la fonction
# Devrait afficher 3
print(unite(153))

# Question 2
def fonction(n):
    a = n // 10
    return (unite(a))

# On test la fonction sur 153 et on voit ce que ca donne
print(fonction(153))
# Cette fonction retourne 5, donc le chiffre des dizaines

# Question 3

# Fonction qui fait les centaines
def centaine(n):
    a = n // 10
    return fonction(a)

# On test la fonction
# Devrait afficher 1
print(centaine(153))

# Question 4

# On definit la fonction Armstrong
def Armstrong(m):
    # On extrait les chiffres
    u = unite(m)
    d = fonction(m)
    c = centaine(m)

    # On calcul la somme des cubes
    somme = u ** 3 + d ** 3 + c ** 3

    # On regarde si elle est egale a m
    return m == somme

# On verifie
print(Armstrong(153)) # Affiche True
print(Armstrong(157)) # Affiche False