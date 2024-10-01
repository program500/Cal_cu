"""class car: 
    _Brand = "Toyota"
    def display(self):
        print(f"Our brand name is {self._Brand}")
class sedar(car):
    def displayformeting(self):                  #procted access modifire 
        print(f"Our brand name is {self._Brand}")
obj = car()
obj.display()
ob = sedar()
ob.displayformeting()"""

class _car : 
    _Brand = "Toyota"
    def display(self):
        print(f"Our brand name is {self._Brand}")
class _soncar(_car): 
    def displayformeting(self):
        print(f"Our brand name is {self._Brand}")
obj = _car()
obj.display()
ob = _soncar()
ob.displayformeting()















