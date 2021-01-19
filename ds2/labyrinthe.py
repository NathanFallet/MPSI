from typing import Any, List

lab=[["1","1","1","1","1","1","1","1"],
    ["1","m","o","m","s","m","o","1"],
    ["1","o","o","o","o","o","o","1"],
    ["1","m","o","m","m","m","o","1"],
    ["1","o","m",'m',"o","o","o","1"],
    ["1","o","o","o","m","o","m","1"],
    ["1","m","o","m","o","o","m","1"],
    ["1","1","1","1","1","1","1","1"]]


def modifie(lab: List[List[str]], x: int, y: int, c: str):
    lab[x][y] = c # On donne la valeur c à l'élement [a][b]


def empile(l: List[Any], a: Any) -> None:
    l.append(a) # On rajoute a à la fin de la liste


def depile(l: List[Any]) -> Any:
    out = l[-1] # On prend le dernier élément
    l = l[:-1] # La liste vaut maintenant tout sauf le dernier élément
    return out # On retourne le dernier élément


def test(lab: List[List[str]], x: int, y: int) -> bool:
    return lab[x][y] in ("o", "s") # On regarde si la valeur en (x, y) vaut "o" ou "s"


def directions(p: List[Any], lab: List[List[Any]], x: int, y: int) -> None:
    for i, j in ((0, 1), (1, 0), (0, -1), (-1, 0)): # Pour chacun des quatres cas :
        # Cas 1 : i = 0, j = 1  Cas 3 : i = 0, j = -1
        # Cas 2 : i = 1, j = 0  Cas 4 : i = -1, j = 0

        if test(lab, x+i, y+j): # Si la case est accessible
            empile(p, lab[x+i][y+j]) # Alors on l'ajoute à la liste des possibilités


def sortie(lab: List[List[str]], i: int, j: int) -> bool:
    p = [(i, j)] # On prend une pile avec la position initiale
    while len(p) > 0:
        x, y = depile(p) # On prend la permière valeure
        if lab[x][y] == "s": # Si c'est la sortie
            return True # On s'arrête
        modifie(lab, x, y, "V") # Sinon, on marque la case comme visitée
        directions(p, lab, x, y) # On ajoute les cases environantes aux possiblités
    
    return False # Si rien n'a été trouvé, on s'arrête


def essai(lab: List[List[str]], i: int, j: int) -> None:
    if not test(lab, i, j): # On regarde si le départ est invalide
        print("Départ non valide") # Si oui, on le dit, et on s'arrête
        return
    if sortie(lab, i, j): # Si on trouve la sortie
        print("Sortie trouvée") # On le dit
    else:
        print("Je suis enfermé") # Sinon, on le dit aussi