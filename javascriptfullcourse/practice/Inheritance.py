#Inheritence type data 
class Grandfather:
    Dhaka  = 10 
    Gopal = 20
def add(self):
    print(f"He  has {self.Dhaka} House in Dhaka")
    print(f"He has {self.Gopal} House in Gopalgonj")

ob = Grandfather()

class father(Grandfather):
    pass

class mother(father):
    pass

class Bigbrother(mother):
    pass

class Bigsister(Bigbrother):
    pass

class brother(Bigbrother):
    pass
class youngersister(Bigsister): 
    pass

ob= Grandfather()
print(Bigbrother.Dhaka)



print(ob.Dhaka)
print(type(ob))
print(type(ob.Dhaka))
print(type(ob.Gopal))



#single line inceritance 
class father: 
    x = 23 
    y = 45
    def add(self): 
        print(self.x+self.y)

class son(father):
    pass
obj = son()
obj.add()
print(obj.add)