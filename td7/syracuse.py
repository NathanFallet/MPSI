def syracuse(m, n):
    if n == 0: # Si on est à u_0, alors
        return m # On renvoie m
    lastN = syracuse(m, n-1) # On stocke dans une variable pour ne pas calculer plusieurs fois
    if lastN % 2 == 0: # Si u_n-1 est pair, alors
        return lastN/2 # On renvoie u_n-1 / 2
    return 1 + 3 * lastN # Sinon, on renvoie 3u_n-1 + 1

def zero_syracuse(m):
    n = 0 # On initialise n à 0
    while syracuse(m, n) != 1: # Tant que u_n != 0
        n += 1 # On tente pour u_n+1
    return n # On renvoie n