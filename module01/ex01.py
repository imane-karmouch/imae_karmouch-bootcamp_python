class GotCharacter:
  first_name=' '
  is_alive=True
  def __init_(self,n,alive):
    self.first_name=n
    self.is_alive=alive
class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    def print_house_words(self):
      print(self.house_words)
    def die(self):
      self.is_alive=False
    
    
    #test
from game import GotCharacter, Stark
arya = Stark("Arya")
print(arya.__dict__)

arya.print_house_words()

print(arya.is_alive)
arya.die()
print(arya.is_alive)

    
