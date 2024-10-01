#mapping or dictionnary type data 
biodata ={
        "name":"Hasip",
        "age":20,
        "address":"Kotalipara"
         
}

print(biodata)

#mapping or dictionnary type data 
data = {
        "Name": "Hasip  ", 
        "age": 20, 
        "city": "Gopalgonj"
}

print(data.keys())
print(data.values())

x = data['age']
print(x)
x = data['Name']
print(x)
print(x)
print(*x)
print(4*x)
c = data.keys()
print(c)
x = data.values()
print(x)
x = data.items()
for i in x:
    print(i) #i have succeed