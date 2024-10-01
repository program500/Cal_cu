"""#tuple type data
fruits = ('apple', 'banana', 'cherry', 'date ', 'berry', 'onion ', 'garlic','watermailo')

for oneitem in fruits:
    print(oneitem)
    
my_list = list(fruits)
print(my_list)

my_set = set(my_list)
print(my_set)
for i in range(8):
    print(i,fruits[i])
             
"""
#Tuple type data  

my_tuple = ('Apple', 'Banana', 'Cherry', 'Berry', 'Coconut','Pear','Mango', 'Guava')
for index , items in enumerate(sorted(my_tuple), start=1):
    print(f"{index}. {items}")
  
print(my_tuple)

for i in range(10): 
    print(i)
print(my_tuple.index("Apple"))
print(my_tuple.count('Banana'))
x = len(my_tuple)
print(x)