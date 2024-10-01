#key word and argument type data alwaya will be dictionary type 
def add_two(**person):
    print(person["age"])
add_two(
         name = "Hasip",
         age  = 20,
         city = "San francisco"
)


#loop use in funtion in paramitars in arguments

def addtwo(**person):
    print(type(person))
    for key,value in person.items():
        print(f'{key}:{value}')

addtwo(
       name = "Hasip",
       age = 20,
       city = "San francisco"
)
      
#key and value items always will be argument type data theis also have to be paramitars type data 
 

def my_first_function(**person):
    print(type(person))
    for key, value in person.items():
        print(f"{key}: {value}")

my_first_function(
                  name = "Abid Hasan",
                  age = 20,
                  city = "San francisco"

)











def my_first_number(*gentalman):
    print(type(gentalman))
    print(id(gentalman))
    for i in gentalman:
        my_first_number("Hasip","Saim","Sazid","Salman")
print(my_first_number)
my_first_number()
      

#key word and argument type data alwaya will be dictionary type 
def add_two(**person):
    print(person["age"])
add_two(
         name = "Hasip",
         age  = 20,
         city = "San francisco"
)


def add_three(**perso):
    print(perso["age"])
add_three(
         name = "Hasip", 
         age = 20,
         city = "san francisco"
)



#key word argument dictionnary type data 
def my_function(**natu):
    print(natu['name'])
my_function(
            name = "Hasip",
            age = 19,
            city = "San  francisco"
)


#keyword argument type data 
def my_fundamentals(a, b ):
    x = a
    y = b 
    adi = x + y 
    sub = x - y  #keyword argument type data 
    mul = x * y 
    div = x / y 
    print(adi, sub, mul, div)
my_fundamentals(2,4)


