#list type data
mylist = ['apple', 'banana', 'cherry', 'berry', 'date', 'onion', 'garlic']
print(['apple'])
print(type(mylist))
print(mylist);


#Access list item type data 
fruits = ['apple', 'banana', 'cherry', 'berry', 'mango']
print(fruits)
my = tuple(fruits)
print(type(my))

print(fruits[0])
print(fruits[-1])
print(fruits[-2])
print(fruits[3])
print(fruits[0:3])
print(fruits[:3])
print(fruits[4:])
print(fruits[4:-1])
print(fruits[:2])
print(fruits[2:])
print(fruits[4:3])



#Change list item type data 
vagi = ['Arum', 'shak', 'bagun ', 'tegum ']
vagi[2] = "Banana" #change list item type data
print(vagi)

vagi[1:3] = "Apple", "Date"
                     #change list item type data 
                     #its can be changed using this method 
print(vagi)

print(type(vagi))

