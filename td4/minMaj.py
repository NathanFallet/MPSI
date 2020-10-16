# On demamnde une chaine de charactères
c = input("Entrez un chaine de charactères : ")

# On initialise une chaine vide
c2 = ""
for i in c:
    # On regarde si on a une minuscule
    if (ord(i) >= 97) and (ord(i) <= 122):
        # On ajoute la majuscule correspondante
        c2 += chr(ord(i) - 32)
    # On regarde si on a une majuscule
    elif (ord(i) >= 65) and (ord(i) <= 90):
        # On ajoute la minuscule correspondante
        c2 += chr(ord(i) + 32)
    # Sinon, on ne fait rien
    else:
        c2 += i

# On affiche le résultat
print(c2)

# On fait la même chose en une seule ligne, bonus pour ceux qui veulent
print("".join([(chr(ord(i) - 32)) if ((ord(i) >= 97) and (ord(i) <= 122)) else (chr(ord(i) + 32)) if ((ord(i) >= 65) and (ord(i) <= 90)) else i for i in c]))

""" Explications version 1 ligne
Qui se décompose en (dans l'ordre d'execution) :
1) for i in c
Parcours la liste

2) A if ((ord(i) >= 97) and (ord(i) <= 122)) else B if ((ord(i) >= 65) and (ord(i) <= 90)) else C
Effectue A si la première condition est vraie, B si la deuxième est vraie, et C sinon
Cela correspond au if, elif, else du code sur plusieurs lignes

3) (chr(ord(i) - 32)); (chr(ord(i) + 32)); i
Transforme le charactère suivant les conditions

4) "".join(A) → Transforme la liste en chaine

Note : Ceci est sûrement l'une des ligne de code les moins lisibles que j'ai écrit
"""