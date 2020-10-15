# On demande la phrase et la lettre
phrase, lettre = input("Entrez une phrase : "), input("Entrez une lettre : ")

# On initialise le nombre d'occurences
occurences = 0
# On effectue une boucle où i prend la valeur de chaque lettre dans la phrase
for i in phrase:
    # Si la lettre observé correspond à la lettre recherché
    if lettre == i:
        # On ajoute une occurence
        occurences += 1

# On affiche le résultat
print("La lettre \"{}\" apparaît {} fois dans la phrase.".format(lettre, occurences))