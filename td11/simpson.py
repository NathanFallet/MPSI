# Créé par René Lapole, le 01/04/2021 en Python 3.2
def sup(f,a,b):
    s=abs(f(a))
    p=(b-a)/10000
    for i in range (0,10001):
         if s < abs(f(a+i*p)):
              s=abs(f(a+i*p))
    return(s)


# méthode de Simpson

def Simpson(f,f4,a,b,e) :
    M=sup(f4,a,b)
    n=int((M*(b-a)**5/(180*2**4*e))**(1/4)+1)
    h=(b-a)/float(n)
    z=(f(a)+f(b))/6
    for i in range(1,n) :
               z=z+f(a+i*h)/3
    for i in range(n) :
              z=z+f(a+(2*i+1)*h/2)*2/3
    return(h*z , n)

# exemple 3 :

def f(x):
    return(1/(1+x))

def f4(x):
    return(24/((1+x)**5))

from math import log

ln2_s=Simpson(f,f4,0,1,10**(-6))

print("valeur machine : ",log(2))
print("valeur Simpson : ",ln2_s)
print("écart : ",log(2)-ln2_s[0])



