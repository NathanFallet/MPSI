#
# Calcul du déterminant d"une matrice pour inverser une matrice
#

# Afficher une matrice
def print_mat(A):
    for i in range(0, len(A)):
        print("| ", end="")
        for j in range(0, len(A[i])):
            print(A[i][j], end="\t")
        print(" |", end="\n")

# Enlever une ligne et une colonne
def removeIJ(A, i, j):
    return [
        [
            A[l][c]
            for c in range(0, len(A[i]))
            if c != j
        ]
        for l in range(0, len(A))
        if l != i
    ]

    # On fait une nouvelle matrice
    #B = []
    #for l in range(len(A)):
    #    # On enlève la i ème ligne
    #    if l != i:
    #        L = []
    #        for c in range(len(A[l])):
    #            # On enlève la j ème colonne
    #            if c != j:
    #                # Ajoute le coefficient
    #                L.append(A[l][c])
    #        # On ajoute la ligne
    #        B.append(L)
    #return B

# Calculer le déterminant
def det(A):
    # Cas d'une matrice 1x1
    if len(A) == 1:
        return A[0][0]
    
    i = 1
    return sum([
        (-1) ** (i+k) * A[i-1][k-1] * det(removeIJ(A, i-1, k-1))
        for k in range(1, len(A)+1)
    ])

    #somme = 0
    #i = 1 # par exemple
    #for k in range(1, len(A)+1):
    #    somme += (-1) ** (i+k) * A[i-1][k-1] * det(removeIJ(A, i-1, k-1))
    #
    #return somme

# Comatrice
def com(A):
    return [
        [
            (-1) ** (i+j) * det(removeIJ(A, i-1, j-1))
            for j in range(1, len(A[i-1])+1)
        ]
        for i in range(1, len(A)+1)
    ]

    #B = []
    #for i in range(1, len(A)+1):
    #    L = []
    #    for j in range(1, len(A[i-1])+1):
    #        L.append()
    #    B.append(L)
    #return B

# Transposé
def transp(A):
    return [
        [
            A[j-1][i-1]
            for j in range(1, len(A[i-1])+1)
        ]
        for i in range(1, len(A)+1)
    ]

    #B = []
    #for i in range(1, len(A)+1):
    #    L = []
    #    for j in range(1, len(A[i-1])+1):
    #        L.append(A[j-1][i-1])
    #    B.append(L)
    #return B

# Multiplier la matrice par un coef
def multiplier(A, a):
    return [
        [
            a * A[i-1][j-1]
            for j in range(1, len(A[i-1])+1)
        ]
        for i in range(1, len(A)+1)
    ]

    #B = []
    #for i in range(1, len(A)+1):
    #    L = []
    #    for j in range(1, len(A[i-1])+1):
    #        L.append(a * A[i-1][j-1])
    #    B.append(L)
    #return B

# Produit
def produit(A, B):
    return [
        [
            sum([
                A[i][k] * B[k][j]
                for k in range(0, len(A[i]))
            ])
            for j in range(0, len(B))
        ]
        for i in range(0, len(A))
    ]

    #C = []
    #for i in range(0, len(A)):
    #    L = []
    #    for j in range(0, len(B)):
    #        s = 0
    #        for k in range(0, len(A[i])):
    #            s += A[i][k] * B[k][j]
    #        L.append(s)
    #    C.append(L)
    #return C

# Inversion avec log
def inverse(A):
    print("Matrice :")
    print_mat(A)
    print("")

    print("Déterminant :")
    d = det(A)
    print(d)

    if d == 0:
        print("Pas inversible")
        return

    print("Inversible ! On continue")
    print("")
    
    print("Comatrice :")
    co = com(A)
    print_mat(co)
    print("")

    print("Transposée :")
    t = transp(co)
    print_mat(t)
    print("")

    print("Inverse :")
    i = multiplier(t, 1/d)
    print_mat(i)
    print("")

    print("Produit avec son inverse :")
    p = produit(A, i)
    print_mat(p)
    print("")

# Tests
print("---\nMatrice 3x3 :\n---")
inverse([
    [1, -1, 2],
    [2, 1, 1],
    [3, 2, 2]
])
print("\n")

print("---\nMatrice 4x4 :\n---")
inverse([
    [1, 0, 1, 1],
    [1, 1, -1, 1],
    [2, 1, 0, 1],
    [1, 2, 1, 1]
])
