def reverse_string(str):
    if (len(str)) == 1: # Si la chaîne est une lettre seule
        return str # On ne fait rien
    hd, tl = str[0], str[1:] # Sinon, on sépare la première lettre (tête) du reste (queue) 
    return reverse_string(tl) + hd # Et on renvoi l'inverse de la queue, suivi de la tête