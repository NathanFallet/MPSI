# On importe les fonctions mathématiques
from math import log, e, atan, pi, sin

# On définit la fonction phi
def phi(x):
    # Dans le cas x < -2
    if x < -2:
        return -2 * log(x, e) + 1

    # Dans le cas x > 5
    elif x > 5:
        return atan(x) - pi

    # Dans le cas -2 <= x <= 5
    else:
        return 4 * sin(x)
