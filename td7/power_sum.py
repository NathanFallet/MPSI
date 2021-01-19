def power_sum(n: int, a: int) -> int:
    if n == 0: # Si n == 0, alors on renvoi 0**a, soit 0
        return 0
    return n**a + power_sum(n-1, a) # Sinon, on renvoi n**a + ∑[k=0][n-1] n**a