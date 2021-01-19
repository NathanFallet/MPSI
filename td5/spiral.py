# On importe matplotlib, ainsi que la fonction choice our les couleurs
from typing import Tuple
import matplotlib.pyplot as mplpp
from random import choice


# On paramètre les axes
mplpp.axis("equal")


# On définit la fonction spirale pour créer la spirale
def spiral(origin: Tuple[float, float], radius: float, amount: int):
    # On définit une liste de couleurs
    colorList = ["xkcd:tan", "xkcd:aqua", "xkcd:lime", "xkcd:gold", "xkcd:light red",
                "xkcd:steel blue", "xkcd:grass", "xkcd:orchid", "xkcd:emerald", "xkcd:pastel pink",
                "xkcd:lemon", "xkcd:light indigo", "xkcd:vermillion", "xkcd:muddy brown", "xkcd:electric pink",
                "xkcd:heliotrope", "xkcd:wisteria", "xkcd:sunflower", "xkcd:royal", "xkcd:ruby",
                "xkcd:vivid blue", "xkcd:ice", "xkcd:greenblue", "xkcd:wintergreen", "xkcd:charcoal grey"]
    
    # On crée les cinq sommets du carré -> Pour que le carré soit fermé quand on relie les points ensemble
    xList = 2 * [origin[0] + radius] + 2 * [origin[0] - radius] + [origin[0] + radius]
    yList = [origin[1] + radius] + 2 * [origin[1] - radius] + 2 * [origin[1] + radius]

    # On répète n fois
    for _ in range(amount):
        # On dessine un carré vide avec la fonction plot()
        mplpp.plot(xList, yList, choice(colorList))

        # On décale de 10% les quatres premiers points de la liste
        for j in range(len(xList)-1):
            xList[j] = (xList[j] * 9 + xList[j+1]) / 10
            yList[j] = (yList[j] * 9 + yList[j+1]) / 10
        
        # Pour le cinquième points, on lui donne la valeur du premier point
        xList[-1] = xList[0]
        yList[-1] = yList[0]
    
    # On affiche le graphique
    mplpp.show()


# On demande à l'utilisateur combien de carrés veut-il et effectue la fonction adequate
spiral((10, 10), 10, int(input("Nombre de carrés : ")))