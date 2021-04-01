# Créé par Rene, le 14/03/2021 en Python 3.2
# pour un système différentielle

from math import *
import matplotlib.pyplot as plt
import numpy as np

def f(x,y,t):
   return x*(3-2*y)

def g(x,y,t):
   return y*(x-4)

def euler2(f,g,x0,y0,t0,t1,n):
  h = (t1-t0)/n
  x = np.zeros(n)
  y = np.zeros(n)
  T=np.zeros(n)
  T[0] = t0
  x[0] = x0
  y[0] = y0
  for i in range(n-1):
     x[i+1] = x[i] + h*f(x[i],y[i],T[i])
     y[i+1] = y[i] + h*g(x[i],y[i],T[i])
     T[i+1] = T[i] + h
  return(x,y,T)


(x,y,T) = euler2(f,g,5,3,0,10,1000)

plt.plot(T,x,"r")
plt.plot(T,y,"y")
plt.show()


# portrait de phase

plt.plot(x,y)
plt.show()


(x,y,T) = euler2(f,g,5,3,0,10,2000)

plt.plot(x,y)
plt.show()


(x,y,T) = euler2(f,g,4,1.501,0,10,1000)
# presque le point fixe !!!!
plt.plot(x,y)
plt.show()



# pour une équation différentielle d'ordre 2


# exemple : y'' = 8*sin(y) - y'/5 avec x0=pi/2 , y0=0, t0=0 et t1=20 avec n= 10000 pas

# qu'on traduit en X' = Y et Y' = 8 sin X - Y/5


def f(x,y,t):
   return y

def g(x,y,t):
   return 8*sin(x) - y/5

(x,y,T) = euler2(f,g,pi/2,0,0,20,10000)

plt.plot(T,y)
plt.show()


