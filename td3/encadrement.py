# On demande un nombre
n = int(input("Entrez un nombre : "))

# On initialise la valeur de l'encadrement
encadrement = 0
# Tant que l'encadrement est trop petit, on l'augmente
while n / (10 ** encadrement) >= 1:
    encadrement += 1

# On affiche le résultat
print("{} se trouve entre 10^{} et 10^{}".format(n, encadrement-1, encadrement))