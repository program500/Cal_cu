#union join set type data 
set1  = {'apple', 'banana', 'cherry','berry'}
set2 = {'mango', 'guava', 'wood apple', 'pine apple'}
set3 = set1.union(set2)       #this is union set type data 
print(set3)

i = {10, 23, 54, 30}
y = {1,2,3,3,4,}
o = i | y     #set join type 
print(o)

#set truple join 
set = {'date', 'ornge','plum'}
set1 = {1,2,3,4,5,6,7,8}
set2 = {'garlic', 'onion', 'banana'}
set3 = {True, False, 'pear'}

z = set.union(set1,set2,set3)
print(z)

s = set | set1 | set2 | set3

print(s)
#set update type data 
x = { 'apple', 'banana', 'cherry', 'berry'}
y = {'wood apple', 'pineapple'}
x.update(y)
print(x)