""" 1) Prendre tout les éléments d'une liste suivant une condition """
# [i for i in liste if condition]

# Exemple : On ne prend que les multiples de 3
print("Exemple du 1) : ")

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([i for i in liste if (i % 3 == 0)]) # Note : les parenthèses sont optionnelles



""" 2) Obtenir une liste contenant les nombres de n à m """
# [*range(n, m+1)]

# Exemple : On prend les nombres de 11 à 20
print("\nExemple du 2) : ")

print([*range(11, 20+1)])



""" 3) Appliquer une transformation aux éléments d'une liste suivant une condition """
# [transformation1 if condition else transformation2 for i in liste]

# Exemple : On prend 10i si i est pair et 2i si i est impair
print("\nExemple du 3a) : ")

liste = [*range(1, 10+1)]
print([((10 * i) if (i % 2 == 0) else (2 * i)) for i in liste]) # Note : les parenthèses sont optionnelles


# Exemple : On divise par deux les nombres pairs, et ne fait rien au reste
print("\nExemple du 3b) : ")

liste = [*range(1, 10+1)]
print([((i // 2) if (i % 2 == 0) else i) for i in liste]) # Note : les parenthèses sont optionnelles



""" 4) Échanger deux variables """
# var1, var2 = var2, var1

# Exemple : On échange a et b
print("\nExemple du 4a) : ")

a = 3
b = 4
print("a =", a)
print("b =", b)

print("On échange")
a, b = b, a

print("a =", a)
print("b =", b)


# Exemple : On échange la première et dernière valeur d'une liste
print("\nExemple du 4b) : ")

liste = [*range(1, 11)]
liste[0], liste[-1] = liste[-1], liste[0]
print(liste)