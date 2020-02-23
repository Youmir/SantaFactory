import unittest
from classes.nain import Nain
from classes.cadeau import Cadeau

class NainTest(unittest.TestCase):

#Example of unittest
# Lancer le nain a emballer et verifier la disponibilite et le temps que ca va lui prendre
    def TestStartWrapGift(self):
        gift = Cadeau("small")
        worker = Nain(1)
        worker.startWrapGift(gift)
        self.assertEqual(worker.IsDispo, False)
        self.assertEquals(worker.dispoAfter,0.5)




if __name__ == "__main__":
    unittest.main()