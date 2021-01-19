def is_palindrome(str: str) -> bool:
    if len(str) <= 1: # Si on a une seule lettre ou si vide, alors c'est un palindrome
        return True
    # On sépare en première, le reste et dernière lettre
    first, middle, last = str[0].lower(), str[1:-1], str[-1].lower() # On met en minuscules
    # On teste si premier = dernier ET si le millieu est un palindrome
    return first == last and is_palindrome(middle)