from threading import Thread
from time import sleep

def boucle1():
    while True:
        print("A")
        sleep(2)

def boucle2():
    while True:
        print("B")
        sleep(3)

Thread(target = boucle1).start()
Thread(target = boucle2).start()