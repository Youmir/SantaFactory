from cadeau import Cadeau
from nain import Nain
from random import randint
from traineau import Traineau



# Class Factory : class pour gerer l'usine du pere noel 
# Contient 4 methodes et 6 attributs 
# self.timer : 
# self.nainIndexToWrap :
# self.traineau : object de class Traineau
# self.numNains : un nombre definit au hasard de nains pour travailler allant de 0 au nombre de cadeaux a faire
# self.gifts : liste d'object de type Cadeau
# self.nains : liste d'object de type Nain


class Factory():

# Constructeur : initialization des attributs de la classe

    def __init__(self,gift_types):
        self.timer = 0
        self.nainIndexToWrap = 0
        self.traineau = Traineau()
        self.numNains = randint(1, len(gift_types))
        print("Number of nains {}".format(self.numNains))
        self.gifts = []
        self.nains = []
        for index in range(len(gift_types)):
            print("Creating a {} gift".format(gift_types[index]))
            self.gifts.append(Cadeau(gift_types[index]))
        for index in range(self.numNains):
            self.nains.append(Nain(index + 1))

# addTime : calcule le temps de travail depuis le demarrage de l'usine
# params : 
#   - time :     
    def addTime(self, time):
        self.timer += time
        print("{} seconds has passed, total: {} seconds".format(time, self.timer))
        for nain in self.nains:
            nain.addTime(time, self.traineau, self)
# checkNain : verifie si le nain est disponible pour commencer a emballer le cadeau sinon passe au nain suivant s'il est pas dispo rajoute un cycle de travail
# params:
#   - gift : object de class Cadeau

    def checkNain(self, gift):
        nain = self.nains[self.nainIndexToWrap]
        if nain.IsDispo:
            nain.startWrapGift(gift)
        else:
            if self.numNains - 1 != self.nainIndexToWrap:
                self.nainIndexToWrap += 1
            else:
                self.addTime(0.5)
                self.nainIndexToWrap = 0
            self.checkNain(gift)

# checkOnHoldNains : verifie si le nain a un cadeau dans les mains et en attente du traineau et lui demande de le mettre dans le traineau

    def checkOnHoldNains(self):
        for nain in self.nains:
            if nain.isOnHold():
                nain.free(self.traineau, self)

# start : la methode principale de l'application et de la class factory.
# params:
#           - Verifie si le traineau est dans l'usine et s'il est vide 
#           - appelle la methode chackNain() de la class Nain
#           - appelle la methode tryToDeliver() de la class Traineau
#           - S'assure a la fin si le traineau est rempli, de liver.

    def start(self,factory):
        for gift in self.gifts:
            if self.traineau.IsHere and self.traineau.IsPlein() == False:
                self.checkNain(gift)
                self.traineau.tryToDeliver(self)
        if self.traineau.IsEmpty() == False:
            self.traineau.deliver(factory)