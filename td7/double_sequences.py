def u(n):
    if n == 0: # On gère n = 0
        return 2
    prev = u(n-1) # On prend u_n-1
    return (prev + 2 / prev) / 2 # Et on calcule u_n en remplaçant v_n-1 par 2 / u_n-1 pour optimiser

def v(n):
    return 2 / u(n) # On définit quand même v_n