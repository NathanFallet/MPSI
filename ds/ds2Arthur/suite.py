# On définit la suite u
def u(n):
    # Si n = 0, alors on retourne 1
    if n == 0:
        return 1
    # Si n = 1, alors on retourne 2
    if n == 1:
        return 2
    # Sinon, on utilise la formule générale pour calculer u(n)
    return 3 * u(n - 1) - 2 * u(n-2)

# Pour chaque entre 0 et 9
for i in range(10):
    # On affiche u(i)
    print("u({}) = {}".format(i, u(i)))