# On importe matplotlib, ainsi que des fonctions mathématique utiles
from typing import Tuple
import matplotlib.pyplot as mplpp
from math import sin, cos, pi
from random import choice


# On paramètre les axes
mplpp.axis("equal")


# On définit une fonction affichant un cercle
# Le "precision = 100", nous permet de préciser optionelement ce paramètre, il vaudra 100 par défaut
def circle(origin: Tuple[float, float], radius: float, precision: int = 100) -> None:
    # On définit une liste de couleurs
    colorList = ["xkcd:tan", "xkcd:aqua", "xkcd:lime", "xkcd:gold", "xkcd:light red",
                "xkcd:steel blue", "xkcd:grass", "xkcd:orchid", "xkcd:emerald", "xkcd:pastel pink",
                "xkcd:lemon", "xkcd:light indigo", "xkcd:vermillion", "xkcd:muddy brown", "xkcd:electric pink",
                "xkcd:heliotrope", "xkcd:wisteria", "xkcd:sunflower", "xkcd:royal", "xkcd:ruby",
                "xkcd:vivid blue", "xkcd:ice", "xkcd:greenblue", "xkcd:wfloatergreen", "xkcd:charcoal grey"]
    
    # On crée une liste de précision éléments entre 0 et 2π 
    pofloatList = [i * (2 * pi / precision) for i in range(precision)]
    # On obtient les coordonnées des pofloats de notre cercle en prenant le sinus/cosinus de chaque pofloat de la liste précédente
    xList = [origin[0] + sin(i) * radius for i in pofloatList]
    yList = [origin[1] + cos(i) * radius for i in pofloatList]

    # On demande à matplotlib de tracer notre cercle, avec une couleur aléatoire de la liste précédente
    mplpp.fill(xList, yList, choice(colorList))


# On définit une fonction pour afficher une cible
def target(origin: Tuple[float, float], radius: float, amount: int) -> None:
    # On crée une liste de n éléments, représentant les rayons décroissants des cercles
    radiuses = [radius - (radius / amount) * i for i in range(amount)]

    # On parcours cette liste pour créer un cercle pour chaque rayon
    for i in radiuses:
        circle(origin, i)
    
    # On affiche le graphique
    mplpp.show()


# On définit une fonction pour afficher les tangeantes floatérieures d'un cercle
def innerTangent(origin: Tuple[float, float], radius: float, amount: int) -> None:
    # On crée une liste de n éléments, représentant les rayons décroissants des cercles
    radiuses = [radius / (2 ** i) for i in range(amount)]
    # On crée une liste de n éléments, représentant les origines de chacun des cercles
    originsX = [origin[0] - radius / (2 ** i) for i in range(amount)]

    # On parcours ces listes pour créer un cercle pour chaque rayon et origine
    for i in range(amount):
        circle((originsX[i], origin[1]), radiuses[i])

    # On affiche le graphique
    mplpp.show()


# On définit une fonction pour afficher les tangeantes floatérieures d'un cercle
def outerTangent(origin: Tuple[float, float], radius: float, amount: int) -> None:
    # On crée une liste de n éléments, représentant les rayons décroissants des cercles
    radiuses = [radius / (2 ** i) for i in range(amount)]
    # On crée une liste de n éléments, représentant les origines de chacun des cercles
    originsX = [origin[0] -  3 * radius / (2 ** i) for i in range(amount)]

    # On parcours ces listes pour créer un cercle pour chaque rayon et origine
    for i in range(amount):
        circle((originsX[i], origin[1]), radiuses[i])
    
    # On affiche le graphique
    mplpp.show()


# On paramètre les axes
mplpp.axis("equal")