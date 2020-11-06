# On importe les fonctions nécessaires
from math import sqrt
from matplotlib.pyplot import plot, show, xkcd, xlim, axis

# On demande les coordonées des x de A et E
x = [float(input("x de A : ")), float(input("x de E : "))]

# On demande les coordonées de y de A et E
y = [float(input("y de A : ")), float(input("y de E : "))]

# On calcule les coordonées de B et les ajoutent aux listes
x.insert(1, (2*x[0] + x[-1])/3)
y.insert(1, (2*y[0] + y[-1])/3)

# On calcule les coordonées de C et les ajoutent aux listes
x.insert(2, (x[0] + x[-1])/2 + (y[0] - y[-1])/(2 * sqrt(3)))
y.insert(2, (y[0] + y[-1])/2 + (x[-1] - x[0])/(2 * sqrt(3)))

# On calcule les coordonées de D et les ajoutent aux listes
x.insert(3, (2*x[-1] + x[0])/3)
y.insert(3, (2*y[-1] + y[0])/3)

print(x, y)

# On paramètre le graphe
plot(x, y, ".-")
xlim(x[0] - 1, x[-1] + 1)
axis("equal")

# Et on l'affiche
show()