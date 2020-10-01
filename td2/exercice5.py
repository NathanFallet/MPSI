# On importe les fonctions maths
from math import round

# Demander la taille
t = float(input("Donnez votre taille en metre : "))

# Demander la masse (et non le poids hein)
m = float(input("Donnez votre masse en kilogrammes : "))

# On calcul l'IMC grace a la formule
imc = m / (t ** 2)

# On arrondi a deux chiffres apres la virgule
imc = round(imc, 2)

# On affiche la phrase
print("Vous mesurez " + str(t) + " m et pesez " + str(m) + " kg, votre IMC vaut " + str(imc))
