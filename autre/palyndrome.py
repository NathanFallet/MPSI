# Fonction qui check
def checkV1(word):
    # On reverse le mot
    word2 = word[::-1]

    # On check l'egalite
    return word.lower() == word2.lower()

# Fonction qui check v2
def checkV2(word):
    # Taille du mot
    size = len(word)

    # On iterate le mot
    for i in range(0, size):
        # On check si la lettre est differente
        if word[i].lower() != word[size-1-i].lower():
            # C'est pas un palyndrome
            return False

    # Tout est ok
    return True

# Test 1
print(checkV1("test"))
print(checkV1("Kayak"))

# Test 2
print(checkV2("test"))
print(checkV2("Kayak"))