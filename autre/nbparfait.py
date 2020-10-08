# On regarde si il est parfait
def parfait(n):
    s = 0
    for k in range(1, round(n/2)+1):
        if n % k == 0:
            s = s + k
    return s == n

# On test les nombres
def list(n):
    l = []
    for i in range(6, n+1):
        if parfait(i):
            l.append(i)
    return l

# On test
print(list(1000))