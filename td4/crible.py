def crible(n):
    L = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            L.append(i)
    return L

n = int(input("Entrez un nombre : "))
print(crible(n))