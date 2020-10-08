# Definition
def chiffres(n):
    # On fait une liste
    list = []

    # Tant que n est plus grand que 0
    while n > 0:
        # On récupère le chiffre des unités
        last = n % 10

        # On le met dans la liste
        list.append(int(last))

        # On divise par 10
        n //= 10

    # On donne la liste finale
    return list

# Test
print(chiffres(1234567))