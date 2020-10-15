# On demande la phrase et la lettre
phrase, lettre = input("Entrez une phrase : "), input("Entrez une lettre : ")

# On initialise la liste d'occurences
occurences = []
# On effectue une boucle où i prend la valeur de chaque rang de la phrase
for i in range(len(phrase)):
    # Si la lettre observé correspond à la lettre recherché
    if lettre == phrase[i]:
        # On ajoute la place de l'occurence
        occurences.append(str(i+1))

# On affiche le résultat
print("La lettre \"{}\" apparaît {} fois dans la phrase.".format(lettre, len(occurences)))
# Le " ".join() donne un string contenant toute les valeurs de occurences, séparés par un espace (" ")
print("Elle apparaît aux places : {}".format(" ".join(occurences)))