# On definit la fonction qui resoud l'equation
def eq2(a, b, c):
    # On calcule le discriminant
    d = b ** 2 -  4 * a * c

    # On regarde le signe du discriminant

    # Positif
    if d > 0:
        # On calcul les racines
        x1 = (-b - d ** (1/2))/(2 * a)
        x2 = (-b + d ** (1/2))/(2 * a)

        # On affiche les solutions
        print("2 solutions", x1, " ", x2)
    
    # Negatif
    if d < 0:
        # Pas de racines
        print("Pas de solution dans R")

    # Nul
    if d == 0:
        # On calcul la racine
        x = -b / (2 * a)

        # On affiche la solution
        print("Une racine double :", x)
