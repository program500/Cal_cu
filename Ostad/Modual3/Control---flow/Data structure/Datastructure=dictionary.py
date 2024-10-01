#Data structure dictionnary type data 
Biodata = {
           "name":"Hasip",
           "age": 20,
           "city":"Dhaka"
}

print(Biodata)
print(Biodata["name"])
print(Biodata["age"])
print(Biodata["city"])
Biodata.update({"name": "Abid"})
print(id(Biodata)) #How to update keys and value in dictionary
print(Biodata)


#Keys value pear type data in dictionary 
Biodata = {
           "name":"Hasip",
           "age": 20,
           "city":"Dhaka"
}
print(Biodata.keys())
print(Biodata.values())
print(Biodata.clear())
print(Biodata.items())

print(Biodata.update({"age":"23,"}))




"""Use case 
storing configaration settling
fast lookups 
staring json data 
organizing records
Nested data struetures


"""

#dictionnary type data 
my_life={
        "Name":"Hasip",
        "City": "Goplagonj",
        "age":20
}

print(my_life.update({"City":"Kotalipara"}))