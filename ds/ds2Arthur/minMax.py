# On importe la valeur infini
from math import inf

# On définit la fonction minMax
def minMax(liste):
    # On définit le minimum et le maximum
    min, max = inf, -inf

    # Pour chaque élément de la liste
    for i in liste:
        # Si il est plus grand que le maximum
        if i > max:
            # Il devient le nouveau maximum
            max = i
        # Si il est petit grand que le minimum
        if i < min:
            # Il devient le nouveau minimum
            min = i
    
    # On retourne la paire min, max
    return min, max
