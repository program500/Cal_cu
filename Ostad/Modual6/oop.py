#This is object oriented programming 

class my_function:
    x = 10 
    y = 20 
    z = 30 
    addition = x + y + z 
obs = my_function()
print(my_function.addition)


class myclass:
    x = 10,"pm"
    y = 11, "pm"
    modu = x + y 
ob = myclass()
print(myclass.modu)


class my_class:
    mydictionary = {
        "name": "Hasip", 
        "age": 20, 
        "city": "San francisco"   #This is object oriented programming how to use in dictionary
    }
myob = my_class()
print(my_class.mydictionary.items())


#I have to use sets type data in objectorinetedprogramming
class my_object:
    my_sets = {'Apple','Banana', 'Cherry', 'Berry',' Wood apple', 'plum', 'watermelon', 'lemon', 'coconut', 'Jackfruit', 'pear', '' }

var = my_object()

print(my_object.my_sets)

class student:
    var ={
        "name": "Hasip", 
        "age": 20, 
        "deparment": "Science",
        "varsityname": "Oxford"

    }

ob = student()
print(student.var.items())



#object and str function type dat a

class person:
    def __init__(self, name, age):
        self.n = name
        self.a = age
p = person("Hasip", 20)
print(p)

   
#the string representation of an object  in str_function
class student:
    def __init__(self, school, km):
        self.schoolname = school, 
        self.kilo = km
x = student("Kushla", 30)
print(x)

class student1:
    def __init__(self, name, age):
        self.n = name, 
        self.a = age
    def __str__(self):
        print(f"({self.n} {self.a})")



