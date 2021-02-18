from typing import Tuple

def suites(n: int) -> Tuple[float, float]:
    def u(n: int) -> float: # Fonction auxiliaire pour calculer u
        if n == 0: # On gère n = 0
            return 2
        prev = u(n-1) # On prend u_n-1
        return (prev + 2 / prev) / 2 # Et on calcule u_n en remplaçant v_n-1 par 2 / u_n-1 pour optimiser
    
    out = u(n) # On calcule u_n
    return (out, 2 / out) # On sort un tuple (u_n, v_n)