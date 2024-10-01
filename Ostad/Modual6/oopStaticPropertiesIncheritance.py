"""class Father: 
    x = 10 
    y = 20                       #self method chara class ke kol korte pari @staticmethod use kore 
    @staticmethod
    def addtwo():
        print(Father.x+Father.y)
class son(Father):
    pass

class child(son):
    pass

Father.addtwo()
son.addtwo()
child.addtwo()


class father: 
    pass 
class son: 
    x = 20 
    y = 24
    @staticmethod
    def addtwo():
        print(son.x+son.y)

son.addtwo()"""


class Father :
    x = 10 
    y = 230 
    def addtwofather(self):
        return self.x+self.y
class son(Father):
    
 def addtwoson(self):
    sum = self.addtwoson() + 100
     
obj = son()
obj.addtwoson()