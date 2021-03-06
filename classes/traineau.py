from random import choices, randint


# Classe Traineau
# contient 5 methodes et 4 attribues 
# self.maxCapacite : capacite maximum du traineau
# self.capacite : poids du traineau a un moment donne, augemente du poids du cadeau mis dans le traineau
# self.numOfGifts : le nombre de cadeau dans le traineau
# self.isHere : la presence du traineau dans l'usine


class Traineau():
    def __init__(self):
        self.maxCapacite = 12
        self.capacite = 0
        self.numOfGifts = 0
        self.IsHere = True

# IsPlein : verifie si le traineau est plein
# retour : True si le traineau est plein, False s'il est vide.


    def IsPlein(self):
        return True if self.capacite == self.maxCapacite else False


# IsEmpty : verifie si le traineau est vide
# retour : True si le traineau est vide, False s'il est plein.: 

    def IsEmpty(self):
        return True if self.capacite == 0 else False

# PutAGift : si le traineau est dans l'usine et que le poids du cadeau n'induira pas un depassement du poids max du traineau,
#            affiche que le cadeau emballe sera deposer dans le traineau, 
#            rajoute le poids du ceadeau dans le poids du traineau et incremente le nombre de cadeau dans le traineau de 1
# retours : True si le cadeau a ete  depose dans le traineau, sinon False
# params:
#       - 

    def PutAGift(self, gift, factory):
        if self.IsHere and self.maxCapacite - self.capacite >= gift._poids:
            print("The {} gift is being put in the traineau".format(gift._type))
            self.capacite += gift._poids
            self.numOfGifts += 1
            return True
        else:
            print("The {} gift is on hold".format(gift._type))
            self.deliver(factory)
            return False

# IsPleain : 
# params:
#       - 

    def tryToDeliver(self, factory):
        if self.IsHere and self.IsEmpty() == False:
            if self.IsPlein():
                self.deliver(factory)
            else:
                ask = input("The traineau has {} gifts weighting {} kgs, Write Y to deliver ".format(self.numOfGifts, self.capacite))
                if ask == "Y":
                    self.deliver(factory)
                else:
                    print("Ok, No delivery!")

# IsPleain : 
# params:
#       - 
    
    def deliver(self, factory):
        luck = choices(["Deliver", "Deliver", "Hungry", "Deliver", "Deliver"])
        if luck[0] == "Deliver":
            print("The rennes will deliver")
            self.IsHere = False
            print("Delivering {} gifts, It will take {} seconds".format(self.numOfGifts, self.numOfGifts*0.5))
            factory.timer += self.numOfGifts*0.5
            print("{} seconds has passed, total: {} seconds".format(self.numOfGifts*0.5, factory.timer))
            self.numOfGifts = 0
            self.capacite = 0
            self.IsHere = True
            factory.checkOnHoldNains()
        else:
            print("The rennes are hungry, we will ask them again")
            self.deliver(factory)