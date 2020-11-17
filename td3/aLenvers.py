# On demande un nombre
n = int(input("Entrez un nombre : "))

# On initialise une liste
list = []
# On répète tant que n est different 
while n != 0:
    # On ajoute le chiffre à la liste
    list.append(n % 10)
    # On supprime le chiffre des unités en le divisant par 10
    n //= 10 # n = n // 10

# On initialise une variable
nombre = 0

# On parcours la liste des chiffres
for j in range(len(list)):
    # Pour chaque nombre, on le multiplie par la puissance de 10 adéquate
    nombre += list[j] * (10 ** (len(list) - j - 1))

# On affiche le résultat
print(nombre)