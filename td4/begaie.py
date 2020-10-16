# On demande une chaine de charactères
string = input("Entrez une chaine de charactères : ")

# On affiche la chaine avec les caractères doublés
print("".join([i + i for i in string]))

""" Décomposition en étapes de la dernière ligne
1) A = [i + i for i in string]
Fabrique une liste contenant pour chaque lettre de la chaine de base, son double
Pour chaque charactère de la chaine, ajouter dans la liste ce charactère plus lui-même
"abc" → ["aa", "bb", "cc"]

2) "".join(A)
Fabrique une chaine de caractères en joignant bout à bout chaque valeur de la liste, avec le charactère "" entre chaque élément (donc aucune séparation)
["aa", "bb", "cc"] → "aabbcc"
"""