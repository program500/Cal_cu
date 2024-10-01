#immutable type data
#1=string
#2=Integer
#3=float
#4=tuple
#5=forzenset
#6=flloting

#string type data 
ha = "Hasip"
ka = "kabir"
su = ha, ka
print(id(su))
print(id(su))

#integer type data 
n = 10 
m = 34
sum = n+m
print(id(sum))
print(id(sum))

#float type data

x = 19.43
y = 34.34
equ = x + y
print(id(equ))
print(id(equ))

#Tuple type data 
My_fruits=('apple','banan', 'cherry', 'barry','date',)
print(id(My_fruits))
print(id(My_fruits))

#frozenset type data 
my_list = frozenset({'orange','jackfruit','plum',})
print(id(my_list))
print(id(my_list))


