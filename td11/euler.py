# Créé par René Lapole, le 01/04/2021 en Python 3.2
#  methode euler

from math import *
def phi(y,t):
    return ((cos(t)/sin(t))*y)

# résoudre l'équation différentielle :
# y'(t)= cos(t)/sin(t) * y(t) avec y(0,01)=0,01
# on calcule et on a pour solution : f:x -> f(x) = 0.01/sin(0.01)sin(t)

import numpy as np
import matplotlib.pyplot as plt

def euler(phi,a,b,y,n):
    h = (b-a)/n
    t = a
    Y = [y]
    Z=[0]
    T = [a]
    K=0.01/sin(0.01)
    for k in range(n):
        y = y + h*phi(y,t)
        t = t + h
        Y.append(y)
        Z.append(K*sin(t))
        T.append(t)
    return T,Y,Z



def des_euler(T,Y,Z):
    plt.plot(T, Y, label="par Euler")
    plt.plot(T, Z, label="0.01/sin(0.01)*sin(t)")
    plt.legend()
    plt.show()


(T,Y,Z)=(euler(phi,0.01,3.14,0.01,100))
(T1,Y1,Z1)=(euler(phi,3.15,6.2,-0.008,100))
(T+T1,Y+Y1)

(T+T1,Y+Y1)

des_euler(T+T1,Y+Y1,Z+Z1)

