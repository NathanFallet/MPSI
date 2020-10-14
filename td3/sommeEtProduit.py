# On demande un nombre
n = int(input("Entrez un nombre : "))

# On initialise k
k = 0
for i in range(1, n+1):
    # On ajout i à k
    k += i # k = k + i

# On affiche k
print(k)

# On ré-initialise k
k = 1
for i in range(1, n+1):
    # On ajout i à k
    k *= i # k = k + i

# On affiche k
print(k)