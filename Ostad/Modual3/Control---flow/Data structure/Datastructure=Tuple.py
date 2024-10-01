#Data structure tuple type data 
fruits = ('Apple ' , 'Banana', 'Cherery')
print(fruits[1])
print(fruits[2])
my_list = list(fruits)
print(my_list)
print(type(my_list))
print(fruits)
print(type(fruits))
print(id(fruits))
print(id(my_list))

#tuple method count 
number = (1,2,3,4,5,6,7,8,9)
value = number.count(5)
print(value)

#slicing tuple type data 
fruits = ('apple', 'banana', 'cherry', 'berry', 'mango')
print(fruits[0:2])
print(fruits[3:])
print(fruits[0:])
print(fruits[0:1]) #this is a sciling type data 
print(fruits[:3])
for item  in fruits:
    print(item)  #i know that how to use for loop 


    #Tuple use case 
    """
    imputable data storage
    return multiple values
    fixed collecting 
    database records
    
    
    """