import numpy
from random import randint
from copy import deepcopy

def mat_aléa(n,p):
    a=numpy.zeros([n,p])
    for i in range(n):
        for j in range(p):
            a[i,j]=randint(0,10)
    return(a)

# Exercice n° 1 : matrices égales

def égales(A,B):
     nl=len(A)
     nc=len(A[0])
     nlb,ncb=len(B),len(B[0])
     if (nl,nc) != (nlb,ncb):
        return(False)
     else:
        for i in range (nl):
            for j in range(nc):
                if A[i,j]!=B[i,j]:
                    return(False)
        return(True)

print("essai exercice n° 1")
a=mat_aléa(2,4)
b=deepcopy(a)
print("__________")
print(a)
print(b)
print("égales :", égales(a,b))
print("")
print("___________")

b[1,3]=-1
print(a)
print(b)
print("égales :", égales(a,b))
print("")
print("___________")

# Exercice n° 2 : transposée d'une matrice

def transposée1(a):
    dim=numpy.shape(a)
    ta=numpy.zeros([dim[1],dim[0]])
    for i in range(dim[1]):
        for j in range(dim[0]):
            ta[i,j]=a[j,i]
    return(ta)

print("essai exercice n° 2")
print("  ")
a=mat_aléa(3,2)
ta=transposée1(a)
print("a=",a," et sa transposée :",ta)

# Exercice n° 3 : somme de deux matrices

def somme(a,b):
   dima=numpy.shape(a)
   dimb=numpy.shape(b)
   if dima != dimb:
      return("incompatibles")
   else:
    s=numpy.zeros(dima)
    for i in range(dima[0]):
        for j in range (dima[1]):
            s[i,j]=a[i,j]+b[i,j]
    return(s)

def produit(a,b):
    d1=numpy.shape(a)
    d2=numpy.shape(b)
    if d1[1]!=d2[0]:
        return("formats incompatibles")
    else:
        p=numpy.zeros([d1[0],d2[1]])
        for i in range(d1[0]):
            for j in range(d2[1]):
                for k in range(d1[1]):
                    p[i,j]=p[i,j]+a[i,k]*b[k,j]
        return(p)

def aff_op(a,b,op):
    d=numpy.shape(a)
    if op=="+":
        r=somme(a,b)
    if op=="x":
        r=produit(a,b)
    for i in range (d[0]):
        if i != d[0]//2:
            print(a[i],"   ",b[i],"   ",r[i])
        else:
            print(a[i]," ",op,b[i]," = ",r[i])

print("essai exercice n° 3")
a=mat_aléa(3,4)
b=mat_aléa(3,4)
s=somme(a,b)
print("   ")
aff_op(a,b,"+")
print(" ")
print("______________")

# Exercice n° 4 : propriétés de la transpostion et de l'addition

def p1(a,b):
    return(égales(transposée1(somme(a,b)),somme(transposée1(a),transposée1(b))))

# Exercice n° 5 : multiplication par un scalaire

def mul_scal(alpha,a):
    dim=numpy.shape(a)
    alphaxa=numpy.zeros([dim[0],dim[1]])
    for i in range (dim[0]):
        for j in range (dim[1]):
            alphaxa[i,j]=alpha*a[i,j]
    return(alphaxa)

# Exercice n° 6 : symétrique - antisymétrique ou ni l'un ni l'autre ?

def sym_antisym(a):
    dim=numpy.shape(a)
    if dim[0]!=dim[1]:
        return("pas carrée donc rien !!!!")
    elif égales(a,transposée1(a)):
        return("symétrique")
    elif égales(a,mul_scal(-1,transposée1(a))):
        return("antisymétrique")
    else:
        return("rien")

print("exercice n°6 : ")
a=numpy.array([[1,2],[2,1]])
b=numpy.array([[0,5],[-5,0]])
print(a)
print("  ")
print(sym_antisym(a))
print("  ")
print(b)
print(sym_antisym(b))
print(" ")
print("______________")

# Exercice n° 7 : décomposition

def décomposition(m):
    s=mul_scal(1/2,somme(m,transposée1(m)))
    a=mul_scal(1/2,somme(m,transposée1(mul_scal(-1,m))))
    return(s,a)

print("exercice n°7 : ")
m=mat_aléa(3,3)
d=décomposition(m)
print("   ")
print(d[0]," ",d[1])

# Exercice n° 8 : produit des deux matrices

# fonction produit plus haut

# donc 3 boucles complexité en O(n^3)

print("exercice n°8 : ")
print("   ")
a=mat_aléa(3,4)
b=mat_aléa(4,3)
p=produit(a,b)
aff_op(a,b,"x")

# Exercice n°9 : produit de matrices et transposition

def prod_transpo(a,b):
    p=produit(a,b)
    tp=transposée1(p)
    ta=transposée1(a)
    tb=transposée1(b)
    tatb=produit(tb,ta)
    test=égales(tp,tatb)
    return(tp,tatb,test)

a=mat_aléa(3,3)
b=mat_aléa(3,3)
r=prod_transpo(a,b)
print(r[0])
print("  ")
print(r[1])
print("  ")
print(r[2])
