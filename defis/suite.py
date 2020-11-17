# On initialise la suite à "1", en tant que premier élément d'une liste, et on demande la valeur de n
suite = ["1"]
n = int(input("Quelle étape de la liste voulez vous voir : "))

# Pour chaque étape jusqu'à l'étape demandée
for j in range(n-1):
    # On ajoute une chaine de charactères vide à la liste, pour y stocker la prochaine étape de la suite
    suite.append("")
    # On initialise une variable continuation, pour garder le compte des entrèes de la liste à ignorer
    continuation = 0

    # Pour chaque charactère de la précédente étape de la liste
    for i in range(len(suite[j])):

        # Si l'on doit ignorer le charactère
        if continuation > 0:
            # On marque que l'on a ignoré
            continuation -= 1
            # On fini cette itération de boucle
            continue

        # On se met dans un try pour éviter les erreurs
        try:
            # Si cette élément est identique au deux suivants (soit 333, 222, 111)
            if suite[j][i] == suite[j][i+1] == suite[j][i+2]:
                # On demande d'ignorer les deux prochains éléments, car on est en train de les traiter dans ce groupe
                continuation = 2
                # On ajoute à la dernière étape de la suite 3 + le nombre observé (33, 32, 31)
                suite[-1] += "3{}".format(suite[j][i])
                # On fini cette itération de boucle
                continue

        # Si il y a une erreur (car on sort de la liste), on ignore
        except IndexError:
            pass

        # On se met dans un try pour éviter les erreurs
        try:
            # Si cette élément est identique au deux suivants (soit 33, 22, 11)
            if suite[j][i] == suite[j][i+1]:
                # On demande d'ignorer le prochain élément, car on est en train de le traiter dans ce groupe
                continuation = 1
                # On ajoute à la dernière étape de la suite 2 + le nombre observé (23, 22, 21)
                suite[-1] += "2{}".format(suite[j][i])
                # On fini cette itération de boucle
                continue
        
        # Si il y a une erreur (car on sort de la liste), on ignore
        except IndexError:
            pass

        # Sinon, on ajoute 1 + le nombre observé à la dernière étape de la suite (13, 12, 11)
        suite[-1] += "1{}".format(suite[j][i])

# On affiche ensuite la dernière étape de la suite
print(suite[-1])