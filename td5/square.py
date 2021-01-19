# On importe matplotlib, ainsi que la fonction choice our les couleurs
from typing import Tuple
import matplotlib.pyplot as mplpp
from random import choice


# On paramètre les axes
mplpp.axis("equal")


# On définit une fonction affichant un carré
def square(origin: Tuple[float, float], radius: float):
    # On définit une liste de couleurs
    colorList = ["xkcd:tan", "xkcd:aqua", "xkcd:lime", "xkcd:gold", "xkcd:light red",
                "xkcd:steel blue", "xkcd:grass", "xkcd:orchid", "xkcd:emerald", "xkcd:pastel pink",
                "xkcd:lemon", "xkcd:light indigo", "xkcd:vermillion", "xkcd:muddy brown", "xkcd:electric pink",
                "xkcd:heliotrope", "xkcd:wisteria", "xkcd:sunflower", "xkcd:royal", "xkcd:ruby",
                "xkcd:vivid blue", "xkcd:ice", "xkcd:greenblue", "xkcd:wfloatergreen", "xkcd:charcoal grey"]
    
    # On crée les quatres sommets du carré
    xList = 2 * [origin[0] + radius] + 2 * [origin[0] - radius]
    yList = [origin[1] + radius] + 2 * [origin[1] - radius] + [origin[1] + radius]

    # On demande à matplotlib de tracer notre cercle, avec une couleur aléatoire de la liste précédente
    mplpp.fill(xList, yList, choice(colorList))


# On définit une fonction pour afficher une cible
def target(origin: Tuple[float, float], radius: float, amount: int):
    # On crée une liste de n éléments, représentant les tailles décroissants des carrés
    sizes = [radius - (radius / amount) * i for i in range(amount)]

    # On parcours cette liste pour créer un carré pour chaque rayon
    for i in sizes:
        square(origin, i)
    
    # On affiche le graphique
    mplpp.show()


# On définit une fonction pour afficher les tangeantes floatérieures d'un carré
def innerTangent(origin: Tuple[float, float], radius: float, amount: int):
    # On crée une liste de n éléments, représentant les tailles décroissants des carrés
    sizes = [radius / (2 ** i) for i in range(amount)]
    # On crée une liste de n éléments, représentant les origines de chacun des carrés
    originsY = [origin[0] + radius / (2 ** i) for i in range(amount)]

    # On parcours ces listes pour créer un carré pour chaque taille et origine
    for i in range(amount):
        square((origin[0], originsY[i]), sizes[i])
    
    # On affiche le graphique
    mplpp.show()


# On définit une fonction pour afficher une tour de carrés
def tower(origin: Tuple[float, float], radius: float, amount: int):
    # On crée une liste de n éléments, représentant les tailles décroissants des carrés
    sizes = [radius / (2 ** i) for i in range(amount)]
    # On crée une liste de n éléments, représentant les origines de chacun des carrés
    originsY = [origin[0] -  3 * radius / (2 ** i) for i in range(amount)]

    # On parcours ces listes pour créer un carré pour chaque taille et origine
    for i in range(amount):
        square((origin[0], originsY[i]), sizes[i])
    
    # On affiche le graphique
    mplpp.show()


# On définit une fonction pour afficher des carrés en escalier
def stairs(origin: Tuple[float, float], radius: float, amount: int):
    # On crée deux liste de n éléments, représentant les origines de chacun des carrés
    originsX = [origin[0] * 2 * (i+1) for i in range(amount)]
    originsY = [origin[1] * 2 * (i+1) for i in range(amount)]

    # On parcours ces listes pour créer un carré pour chaque origine
    for i in range(amount):
        square((originsX[i], originsY[i]), radius)
    
    # On affiche le graphique
    mplpp.show()


# On définit une fonction pour afficher des carrés en carré
# Un carré de taille 10 posséde 36 carrés (9 * 4) et non 40 -> d'où le (n-1)
def squareSquared(origin: Tuple[float, float], radius: float, amount: int):
    # Quatres fois, on crée n-1 carrés en avançant l'origine à chaque fois, puis on change la direction
    # Le charactère "_" est utilisé plutôt que "i", pour montrer que sa valeur n'est pas utilisée
    for _ in range(amount-1):
        square(origin, radius)
        origin = (origin[0], origin[1] + 2 * radius)
    for _ in range(amount-1):
        square(origin, radius)
        origin = (origin[0] + 2 * radius, origin[1])
    for _ in range(amount-1):
        square(origin, radius)
        origin = (origin[0], origin[1] - 2 * radius)
    for _ in range(amount-1):
        square(origin, radius)
        origin = (origin[0] - 2 * radius, origin[1])
    
    # On affiche le graphique
    mplpp.show()


# On définit une fonction pour afficher une pyramide de carrés
def pyramid(origin: Tuple[float, float], radius: float, amount: int):
    # On garde en mémoire l'origine de la pyramide
    originalOrigin = origin

    # Pour chaque étage de la pyramide
    for i in range(amount):
        # On remet la variable origin à la valeur néccessaire pour le début de la ligne
        origin = originalOrigin

        # Pour chaque carré de cette ligne, on crée un carré, et avance l'origine pour le carré suivant
        for _ in range(i):
            square(origin, radius)
            origin = (origin[0] + 2 * radius, origin[1])
        
        # On décale l'origine initiale pour la ligne suivante
        originalOrigin = (originalOrigin[0] - radius, originalOrigin[1] - 2 * radius)
    
    # On affiche le graphique
    mplpp.show()


# On définit une fonction pour afficher une spirale de carrés
def spiral(origin: Tuple[float, float], radius: float, amount: int):
    # On répete pour chaque ligne/colomne de la spirale, en partant du centre
    for i in range(amount):
        # On créer une ligne de i carrés, en créeant un carré puis bougeant l'origine pour le carré suivant
        # On utilise une chaîne de if/elif avec un modulo pour changer la direction de la ligne/colomne de manière cyclique
        if (i % 4 == 0):
            for _ in range(i):
                square(origin, radius)
                origin = (origin[0], origin[1] + 2 * radius)
        elif (i % 4 == 1):
            for _ in range(i):
                square(origin, radius)
                origin = (origin[0] + 2 * radius, origin[1])
        elif (i % 4 == 2):
            for _ in range(i):
                square(origin, radius)
                origin = (origin[0], origin[1] - 2 * radius)
        elif (i % 4 == 3):
            for _ in range(i):
                square(origin, radius)
                origin = (origin[0] - 2 * radius, origin[1])
        
    # On affiche le graphique
    mplpp.show()