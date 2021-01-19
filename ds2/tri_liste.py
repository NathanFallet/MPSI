from typing import Any, Tuple

def min_max(l: list[Any], a: int, b: int) -> Tuple[int, int]:
    partie = l[a:b] # On prend la sous-partie nécessaire

    Min, Max = 0, 0
    for i in range(len(partie)): # Pour chaque élément de la liste
        if partie[i] > partie[Max]: # On regarde si c'est le maximum
            Max = i
        
        if partie[i] < partie[Min]: # On regarde si c'est le minimum
            Min = i
    
    return Min+a, Max+a # On ajoute a car on a décalé les indices de -a en prenant une partie


def permute(l: list[Any], a: int, b: int) -> None:
    l[a], l[b] = l[b], l[a] # Un assignement double permet de faire cela en une ligne


def tri(l: list[Any]) -> list:
    for i in range(len(l)//2): # Pour une moitié de liste (on traite les éléments 2 par 2)
        Min, Max = min_max(l, i, -1-i) # On cherche le min et le max
        permute(l, i, Min) # On met le min à sa place
        permute(l, -1-i, Max) # On met le max à sa place
    
    return l # On retourne la liste triée