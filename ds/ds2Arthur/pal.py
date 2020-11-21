# On définit une fonction pal
def pal(chaine):
    # Pour la moitié des élément de la chaine
    for i in range(len(chaine)//2):
        # On regarde si il sont identique à l'élément "symétrique", sans se soucier de la casse
        if chaine[i].lower() != chaine[len(chaine)-1-i].lower():
            # Si non, on retourne faux
            return False
    
    # Si aucun des élément est faux, on retourne vrai
    return True
