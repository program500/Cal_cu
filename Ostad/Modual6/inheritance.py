class Grandfather:  
    x = 10 
    y = 30 
    def addtwo(self):
        print(self.x+self.y)
    def mul(self):
     print(self.x*self.y)
    def sub(self):
     print(self.x-self.y)
    def div(self):
     print(self.x/self.y)

class Father(Grandfather):
    pass
class Mother(Father):        #Python inchertance type data 
    pass 
class son(Mother) :
    pass
class son_child(son):
    pass 

obj = Grandfather()
obj.addtwo()
obj.div()
obj.mul()
obj.sub()


