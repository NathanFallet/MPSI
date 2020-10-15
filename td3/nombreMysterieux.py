# On importe les fonctions
from random import randint

# On défini la fonction de jeu
def nombreMysterieux(nombre):
    # On initialise le nombre d'essais
    essais = 1
    while True:
        # On demande un nombre
        reponse = int(input("Entrez un nombre : "))
        # On regarde si le nombre est plus grand ou plus petit
        if reponse < nombre:
            print("Non, c'est plus grand !")
        elif reponse > nombre:
            print("Non, c'est plus petit !")
        # Si aucun des deux sont bon, alors on sort de la fonction le nombre d'essais 
        else:
            return essais
        # Sinon, on rajoute un essai
        essais += 1

# On demande la borne supérieure
n = int(input("Entrez le nombre maximum : "))
# On lance la fonction
essais = nombreMysterieux(randint(1, n))
# On affiche le nombre d'essais utilisé
print("Gagné en {} essais !".format(essais))