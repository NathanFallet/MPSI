# Fonction qui reverse un mot
def reverse(word):
    # On cree le nouveau mot
    new = ""

    # On iterate le mot d'origine
    for char in word:
        # On ajoute au nouveau mot a la fin
        new = char + new

    # On return le nouveau mot
    return new

# Phase de test
print(reverse("Emilien"))