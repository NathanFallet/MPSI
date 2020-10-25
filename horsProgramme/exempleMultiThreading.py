# On importe les librairies
from threading import Thread
from time import sleep

# On définit une première boucle qui affiche "A" toutes les 2 secondes
def boucle1():
    while True:
        print("A")
        sleep(2)

# On définit une seconde boucle qui affiche "B" toutes les 3 secondes
def boucle2():
    while True:
        print("B")
        sleep(3)

# On lance chacune des deux boucles sur un thread différent
Thread(target = boucle1).start()
Thread(target = boucle2).start()

# 5 secondes après le lancement des deux boucles, on affiche "C"
sleep(5)
print("C")