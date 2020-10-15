# On demande un nombre
n = int(input("Entrez un nombre : "))

# On regarde si n répond aux conditions d'année bissextile
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    # On affiche la réponse
    print("{} est une année bissextile".format(n))
# Dans le cas échéant
else:
    # On affiche que c'est incorrect
    print("{} n'est pas une année bissextile".format(n))