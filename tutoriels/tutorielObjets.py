"""
Un objet est composé de deux composantes principales :
 - des attributs, qui sont des variables qui lui sont propres.
 - des méthodes, qui sont des fonctions qui lui sont propres.

Les objets se définissent en deux temps :
 - d'abord la définition de l'objet en lui-même, on l'on définit comment l'objet marche.
 - puis la définition de ses instances, ses membres, qui vont chacun évoluer différement.

Faisont un exemple avec des animaux :
"""

# On créer une classe d'objet Animal
from typing import Any, List, Tuple


class Animal:
    # La méthode __init__ est la méthode qui est éxécutée lors de la création de l'objet
    # On y initialise tout paramètre de l'objet, souvent aux valeurs des paramètres donnés
    # Ici, self représente l'objet en lui même, self.name représente la variable name propre à l'objet
    def __init__(self, name: str, species: str, age: int) -> None:
        self.name = name
        self.species = species
        self.age = age
    
    # Ensuite, on définit une méthode pour faire viellir l'animal
    # Et ne prend pas de paramètre, car self est fourni automatiquement
    # De plus, on ne peut pas créer une fonction sans avoir self en paramètre, même si l'on ne se sert pas
    def incrAge(self) -> None:
        self.age += 1

    # Pour finir, on définit la fonction __str__, qui s'effectue automatiquement lorsque l'on essaye de transformer l'objet en string
    # Elle est très souvent utilisé pour permettre d'afficher quelque chose de propre et clair quand on print l'objet
    def __str__(self) -> str:
        return "{} est un {} de {} ans.".format(self.name, self.species, self.age)

print("Jouons avec un animal")
animalOne = Animal("Jean-Claude", "chat", 8) # On définit un animal, nommé Jean-Claude, qui est un chat, et a 8 ans
print(animalOne) # On affiche son status via un print
animalOne.incrAge() # On le fait viellir en appelant la méthode correspondante
print(animalOne) # On regarde à nouveau son status
print(animalOne.species) # On demande à afficher que son éspèce
animalOne.name = "Jean-François" # On change son nom
print(animalOne)
print()

"""
Imaginont que nous voulont créer un objet spécifique pour les chats, pour leurs donner des charactéristiques unique aux chats.

Nous n'avons pas besoin de recopier tout le code précedent, mais à la place, on peut faire hérité le code actuel de Animal à notre classe Cat.
Ainsi, Cat aura toujours les fonctions incrAge et __str__, mais on pourra rajouter de nouveaux attributs et méthodes unique aux chats.
"""

# On définit ainsi def Fille(Mère) pour faire hériter les propriétés de Mère à Fille
class Cat(Animal):
    # On recréer une fonction __init__, mais sans le paramètre species, car on sait déjà que c'est un chat
    # On peut rajouter de nouveau paramètes, comme sa couleur, et si il est en train de dormir ou non
    def __init__(self, name: str, age: int, color: str) -> None:
        # En utilisant super().__init__, on appelle le __init__ de Animal
        # On lui passe nos paramètres d'entrée, sauf color, car pas pris en charge par Animal
        # Et pour species, on lui fourni "chat", car un chat est forcément de l'éspèce chat
        super().__init__(name, "chat", age)
        self.color = color
        self.sleeping = False # Un chat commencera toujours éveillé
    
    # On définit une nouvelle méthode unique aux chats, pour miauler
    def meow(self) -> None:
        print("Miaou")
    
    # On définit une fonction pour faire dormir le chat
    def goToSleep(self) -> None:
        self.sleeping = True

    # On définit une autre méthode, pour définir ce qu'un chat fait au réveil
    def wakeUp(self) -> None:
        if not self.sleeping: # Si le chat ne dort pas
            return # Alors on arrête la fonction, car on ne peut pas se réveiller si l'on ne dort pas
        
        self.sleeping = False
        for _ in range(10):
            self.meow()

print("Jouons avec un chat")
catOne = Cat("Jean-Michel", 6, "grey") # On créer notre chat
print(catOne) # On affiche son status, avec la méthode __str__ hérité de Animal
catOne.goToSleep() # Il va dormir
catOne.incrAge() # Il veilli d'un an pendant son sommeil, grâce à la méthode incrAge hérité de Animal
catOne.wakeUp() # Le chat se réveille, et miaule, beaucoup
print(catOne) # Et l'on peut voir qu'il a veilli de 1 an
catOne.wakeUp() # On essaie de réveiller le chat, mais rien ne se passe car il est déjà debout
print()

"""
Beaucoup de fonctions communes peut être remplacés, on a vu comment le faire avec str(), mais il y en a plein d'autres

# Opérateurs arithmétiques
>>> __add__(self, other) -> self + other
>>> __iadd__(self, other) -> self += other
>>> __radd__(self, other) -> other + self
>>> __riadd__(self, other) -> other += self

>>> __mul__(self, other) -> self * other
>>> __floordiv__(self, other) -> self // other
>>> __truediv__(self, other) -> self / other # Attention, les variantes sont __idiv__, __rdiv__, et __ridiv__
>>> __sub__(self, other) -> self - other
>>> __pow__(self, other) -> self ** other
>>> __mod__(self, other) -> self % other
>>> __divmod__(self, other) -> divmod(self, other)
>>> __matmul__(self, other) -> self @ other
>>> __lshift__(self, other) -> self >> other
>>> __rshift__(self, other) -> self << other
>>> __and__(self, other) -> self & other
>>> __or__(self, other) -> self | other
>>> __xor__(self, other) -> self ^ other


# Opérateurs arithmétiques unaires
>>> __pos__(self) -> +self
>>> __neg__(self) -> -self
>>> __abs__(self) -> abs(self)
>>> __invert__(self) -> ~self


# Comparaisons, doit retourner un booléen
>>> __lt__(self, other) -> self < other
>>> __gt__(self, other) -> self > other
>>> __le__(self, other) -> self <= other
>>> __ge__(self, other) -> self >= other
>>> __eq__(self, other) -> self == other
>>> __ne__(self, other) -> self != other


# Changement de type, doit retourner quelque chose du type demandé
>>> __int__(self) -> int(self)
>>> __float__(self) -> float(self)
>>> __complex__(self) -> complex(self)
>>> __list__(self) -> list(self)
>>> __bool__(self) -> bool(self) ou if self:


# Accés aux éléments
>>> __getitem__(self, key) -> self[key]
>>> __setitem__(self, key, other) -> self[key] = other
>>> __len__(self) -> len(self)
>>> __contains__(self, other) -> other in self # Doit retourner un booléen

# Divers
>>> __call__(self, args) -> self(args)


Exemple d'un objet grille :
"""

# On créer une classe Grid, pour définir des grilles
class Grid:
    # On initialise l'objet, avec grid une liste de liste d'éléments
    # On calcule le nombre de ligne et de colonnes
    def __init__(self, grid: List[List[Any]]):
        self.grid = grid
        self.lines = len(grid)
        self.columns = len(grid[0])
    
    # On définit la fonction __getitem__, qui prend deux entiers en entrée
    # Ainsi, on marquera obj[index1, index2]
    def __getitem__(self, key: Tuple[int, int]) -> Any:
        return self.grid[key[1]][key[0]]
    
    # On fait la même chose pour le __setitem__
    def __setitem__(self, key: Tuple[int, int], other) -> None:
        self.grid[key[1]][key[0]] = other
    
    # On définit la transformation en string
    # On retourne chaque ligne séparé par un \n, soit un retour à la ligne
    def __str__(self) -> str:
        return "\n".join([str(i) for i in self.grid])

gridOne = Grid([[2, 3, 4],
                [5, 6, 7],
                [8, 9, 1]])

print("Jouons avec une grille")
print(gridOne) # On commence par afficher la grille
print(gridOne[1, 2]) # On affiche l'objet x=1, y=2
print(gridOne[2, 0]) # On affiche l'objet x=2, y=0
gridOne[1, 1] = 0 # On change la valeur du millieu
print(gridOne) # On affiche la grille pour voire le résultat