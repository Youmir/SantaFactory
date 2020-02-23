import sys
from classes.factory import Factory
from random import choices


## Ceci est un test technique python
## Le but c'est de creer une appli pour aider Santa a' gerer son usine de cadeaux
## L'appli contient 4 classes (Cadeau, factory, nain, Traineau) et ce fichier pour demarrer l'usine
## pour demarrer l'usine lancer la commande : python noel.py <arg:nombre de cadeau>
## Si vous renseignez pas le nombre de cadeau, l'usine demarrera avec 15 cadeaux par defaut
## 
## 
## desole pour l'abscence des accents dans les commentaires, j'ai un clavier qwerty !
##
##


if __name__ == "__main__":

    if len(sys.argv) == 2:
        n_gifts = int(sys.argv[1])
    else:
        n_gifts = 15
    gift_types = choices(["small", "medium", "large"], k=n_gifts)

    factory = Factory(gift_types)
    factory.start(factory)
