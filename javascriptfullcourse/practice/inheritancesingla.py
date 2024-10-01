"""""""""class person:
    name = "Hasip"
    age = 20 
    def add(self):
        print(self.name)
class son(person):
    pass
obj = son
print(obj.name)
print(obj.add)
print(type(obj.add))

#constructor 
class my:
    Ban = 98
    Eng = 89
    def __init__(self):
        print(self.Ban+self.Eng)

ob = my()

print(ob.Eng)
print(ob.Ban)




#Multiple inheritance type data 
class father: 
    x = 20 
    y = 30 
def add(self):
    print(self.x+self.y)
def mul(self):
    print(self.x*self.y)
def sub(self):
    print(self.x-self.y)
def div(self):
    print(self.x/self.y)
ob = father()
class son(father):
    pass
obj = son()

"""
"""
class person:
    name = "Hasip"
    age = 20
    city = "Dhaka "
def add(self):
    pass
ob =person()
print(ob.age)
print(ob.name)
print(ob.city)
""""""

my_tuple = ('apple', 'banan', 'cherry', 'berry')
s = iter(my_tuple)
print(next(s))
print(next(s))
print(type(next(s)))

#constractor in python 

class Member:
    def __init__(self, name, age, city):
       self.name = name
       self.age = age 
       self.city = city 
ob = Member("Hasip", 20, "Sanfrancisco")

print(ob.age)
s = (ob.name, ob.age , ob.city)
for i in s:
    print(i)



#python constructor type data

class person:
    def __init__(self, name, address, phonenumber):
        self.name = name 
        self.address = address
        self.phonenumber = phonenumber 
ob = person("Abid Hasan", "KOtalipara , Gopalgonj", 12343435445)
print(ob.name)
print(ob.address)
print(ob.phonenumber)
s_ = ( ob.name, ob.address, ob.phonenumber)
for items in range:

    print(items, s(items))


    """

#What is constructor how to use constructore 
"""
class person: 
    def __init__(self, name , age, address, phonenumber):
        self.name = name 
        self. age = age 
        self. address = address
        self.phonenumber = phonenumber
ob = person("Hasip", 20, "Dhaka", 999999786767)
s = (ob.name, ob.address, ob.age, ob.phonenumber)
for i in s:
    print(i)
"""
#This is constructtor type data 
"""

class person: 
    def __init__(self, name,  gender, age,  address, city):
        self.name = str(input( "Enter your name: "))
        
        self.gender = str(input( "Enter your gender: "))
    
        self.age = int(input( "Enter your age: "))
    
        self.address = str(input( "Enter your address: "))
        
        self.city = str(input( "Enter your city: "))
        
ob = person(str(input("Enter your name: ")))
ob1 = person(str(input("Enter your gender: ")))
ob2 = person(int(input("Enter your age:  ")))
ob3 = person(str(input("Enter your address: ")))
ob4 = person(str(input("Enter your city: ")))
print(f"My name is {ob.name}")
print(f"I am  {ob1.gender}")
print(f"My old is  {ob2.age}")
print(f"My address is  {ob3.address}")
print(f"My city is {ob4.city}")
#This is constructor type data 

"""
#inheritance in python 
class GrandFather: 
    property = 300
    House = 200
    Shop = 100
    def  add(self): 
        my_tuple = (self.property,self.House,self.Shop)
        for index, items in enumerate(sorted(my_tuple), start=1): 
            print(f"{index}. {items}")
class Father(GrandFather): 
    x = 10 
    y = 34 
    z = 23 
    def addition(self): 
        print(self.x+self.y+self.z) 
        print(self.add,self.addition)
class son(Father, GrandFather): 
    pass 
ob = son()
oj = GrandFather() 
print(ob.addition())
print(ob.add())