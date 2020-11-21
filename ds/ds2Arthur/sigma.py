# On définit la fonction sigma
def sigma(n):
    # On définit une variable de résultat de la somme
    output = 0
    # On fait pour chaque valeur de i tel que 1<=i<=n
    for i in range(1, n+1):
        # On fait pour chaque valeur de j tel que i<j<=n
        for j in range(i+1, n+1):
            # On ajoute le résultat à la somme
            output += i * (j ** 2)
    
    # On retourne la somme
    return output
