# Class Nain contient 4 arguments et 5 methodes et permet de creer des nains a chaque demarrage de l'usine
# les arguments de la classe sont : 
# id : type integer, contient l'id de chaque nain cree
# IsDispo : type Boolean, sert a verifier la disponibilite  du nain
# dispoAfter : type float, calcule le temps restant au nain pour emballer un cadeau 
# actualWrappingGift : type Cadeau, le cadeau sur lequel le nain travail 


class Nain():

# Constructeur : intialization du nain
    def __init__(self, id):
        self.id = id
        self.IsDispo = True
        self.dispoAfter = 0
        self.actualWrappingGift = None

# addTime : 
# params:
#        - time : 
#        - traineau : object de class traineau
#        - factory : object de class factory
    def addTime(self, time, traineau, factory):
        self.dispoAfter -= time
        if self.dispoAfter == 0:
            self.finishWrapGift(traineau, factory)

# startWrapGift : lance un nain l'emballage d'un cadeau, le rend indisponible et indique qu'il sera disponible apres le temps necessaire pour l'emballage du cadeau selon le type
# params :
#      - gift : type Cadeau, le cadeau a emballer

    def startWrapGift(self, gift):
        print("Nain {} is starting to wrap a {} gift, he will finish after {} seconds".format(self.id, gift._type, gift._temps))
        self.actualWrappingGift = gift
        self.IsDispo = False
        self.dispoAfter = gift._temps

# finishWrapGift : affiche que le nain a terminer son travail sur le cadeau et demande au nain de deposer le cadeau dans le traineau
# params :
#         - traineau : objet de classe traineau
#         - factory : objet de classe factory

    def finishWrapGift(self, traineau, factory):
        print("Nain {} has finished to wrap the {} gift".format(self.id, self.actualWrappingGift._type))
        self.free(traineau, factory)

# inOnHolde : verifie si le nain attend le retour du traineau pour deposer son cadeau

    def isOnHold(self):
        return True if self.IsDispo == False and self.dispoAfter == 0 else False


# free : appelle la methode PutAGift() de la classe traineau pour que le nain depose le cadeau et le rend disponible et qu'il ne travaille sur aucun cadeau
# params :
#         - traineau : objet de classe traineau
#         - factory : objet de classe factory

    def free(self, traineau, factory):
        if traineau.PutAGift(self.actualWrappingGift, factory):
            self.IsDispo = True
            self.actualWrappingGift = None