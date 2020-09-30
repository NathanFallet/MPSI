# Question 1

# On definit la fonction qui fait la conversion
def conversion(h, m, s):
    # On converti
    return s + m * 60 + h * 3600

# On test notre fonction
# Ceci devrait afficher 5415
print(conversion(1, 30, 15))

# Question 2

# On demande les deux horaires

# La premiere
print("Horaire 1 :")
h1 = int(input("h = "))
m1 = int(input("m = "))
s1 = int(input("s = "))

# La deuxieme
print("Horaire 2 :")
h2 = int(input("h = "))
m2 = int(input("m = "))
s2 = int(input("s = "))

# On converti
conversion1 = conversion(h1, m1, s1)
conversion2 = conversion(h2, m2, s2)

# On fait la difference
difference = abs(conversion1 - conversion2)

# On affiche le resultat
print("La duree en secondes entre les deux horaires est " + str(difference) + " s")