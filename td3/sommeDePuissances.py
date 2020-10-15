# On demande les deux nombres (double assignation : a, b = c, d; correspond à a = c et b = d)
n, m = int(input("Entrez n : ")), int(input("Entrez m : "))

# On initialise la somme
somme = 0
# On démare la boucle
for i in range(n):
    # On ajoute le résultat
    somme += i ** m # somme = somme + i ** m

# On affiche le résultat
print("Le résultat est : {}".format(somme))