
# Class Cadeau contient 3 arguments et aucune methodes.
# _type : type de cadeau (small, medium, large)
# _poids : poids du cadeau selon _type (small : 1kg , medium : 2kg , large : 5kg) 
# _temps : temps de preparation selon  _type (small : 0.5s, medium : 1s , large : 2s) 

class Cadeau():
    def __init__(self, type):
        self._type = type
        if type == "small":
            self._poids = 1
            self._temps = 0.5
        if type == "medium":
            self._poids = 2
            self._temps = 1
        if type == "large":
            self._poids = 5
            self._temps = 2